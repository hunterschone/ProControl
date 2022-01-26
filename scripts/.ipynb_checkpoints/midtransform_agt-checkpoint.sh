#!/bin/sh
#
# Finds the half-way inbetween space
# Can be used to produce a target that is equally far away from all other images
# 
# AUHTOR
# Jan Scholz @ FMRIB
# Adam Thomas @ FMRIB
#
# DATE
# Nov 2010
# 
# 
set -e

VERSION=0.1

### FUNCTIONS #######################################################

usage ()
{
  echo
  echo "Usage: `basename $0` [-a|r] [-m T1|FA|configfile] [-o AVERAGE] IMAGES..."
  echo
  echo "  -a           use only affine registration"
  echo "  -r           use only rigid registration"
  echo "  -m MODALITY  image modality (default: T1)"
  echo "  -o AVERAGE   output average of halfway transformed images"
  echo "  IMAGES       two or more images"
  echo
  echo "  -q           use queue if possible"
  echo
  echo "version $VERSION"
  echo
  return
}

### MAIN ###############################################
# T1 on pepper takes real 121, sys 45
HOWLONG=150
MODALITY="T1"
queue=0
sinc=0
trilinear=0
if [ "x$FLIRTOPS" = "x" ];then FLIRTOPS="-nosearch";
else
    echo  "!!!!! FLIRTOPTS SET TO $FLIRTOPS !!!!!"
fi

while getopts arqtm:qo: opt; do
    case "$opt" in
	a)  REG="-a"; HOWLONG=5;;
	r)  REG="-r"; HOWLONG=5;;
	q)  queue=1;;
	t)  trilinear=1;;
	i)  sinc=1;;
	o)  average="$OPTARG";;
	m)  MODALITY="$OPTARG";;
    esac
done
shift `expr $OPTIND - 1`

case "$MODALITY" in
#	"T1")  HOWLONG=60; FNIRTCNF='--config=T1_2_MNI152_2mm';;
    "T1")  HOWLONG=60; FNIRTCNF='--config=T1_2_T1_level1';;
    "FA")  HOWLONG=30; FNIRTCNF='--config=FA_2_FMRIB58_1mm';;
    *)     HOWLONG=60; FNIRTCNF="--config=$MODALITY"; echo "using fnirt option $FNIRTCNF";;
esac

[ $# -lt 2 ] && usage && exit 1


##############################################################################
# Register to first image (T)
##############################################################################
addmats=""; addwarps="";
queuefile="midsp_reg_$$"
/bin/rm -f $queuefile
T=`${FSLDIR}/bin/remove_ext $1`; shift

for g in $@; do
#    if [ `${FSLDIR}/bin/imtest $g` -eq 0 ]; then echo "not an image file: $g"; exit 1; fi
    totarget="`basename \`${FSLDIR}/bin/remove_ext $g\``_to_`basename $T`"
    echo "/misc/data19/schonehr/ProControl/scripts/fsl_reg_agt $g $T $totarget $REG -fnirt $FNIRTCNF -flirt \"$FLIRTOPS\";" >> $queuefile
    echo "/misc/data19/schonehr/ProControl/scripts/fsl_reg_agt $g $T $totarget $REG -fnirt $FNIRTCNF -flirt \"$FLIRTOPS\";"
    addmats="$addmats ${totarget}.mat"
    addwarps="$addwarps ${totarget}_warp"
done
chmod a+x $queuefile

# decide whether to send to queue or not
if [ $queue -eq 1 ]; then
    mkdir -p logs
    id=`$FSLDIR/bin/fsl_sub -N midsp_reg -l logs -t ./${queuefile}`
    echo "Registration of $# images to \"$T\": ID=$id"
    sleep 2; 
    while qstat | grep midsp_reg > /dev/null; do sleep 10;echo -n .; done
    sleep 20
    if [ -s ${queuefile}.e${id} ]; then echo error occured; exit 1; fi
else
    echo "Registration of $# images to \"$T\"."
    ./$queuefile
fi


##############################################################################
# Convert warps
##############################################################################

if [ "$REG" != '-a' ] && [ "$REG" != '-r' ]; then
    echo coverting warps
    for w in $addwarps; do
	convertwarp -w $w -o ${w} --relout -r $T
    done
    echo "Converted warps to relative format"
fi
 
##############################################################################
# Misc
##############################################################################
echo converting transformations
target2c="${T}_to_midsp"

if [ "$REG" != '-a' ] && [ "$REG" != '-r' ]; then
    echo nonlin
    ${FSLDIR}/bin/fslmaths `echo $addwarps | sed 's/ / -add /g'` -div `expr $# + 1` -mul -1 ${target2c}_warp
    ${FSLDIR}/bin/convertwarp -w ${target2c}_warp --jstats --constrainj -r $T -o ${target2c}_warp
    ${FSLDIR}/bin/applywarp -i $T -r $T -w ${target2c}_warp -o ${target2c}
else
    if [ $# -gt 1 ]; then
	midtrans -o ${target2c}.mat $addmats
	${FSLDIR}/bin/convert_xfm -omat ${target2c}.mat -inverse ${target2c}.mat
    else
		# backward half transform
	${FSLDIR}/bin/avscale $addmats | awk 'NR>=23 && NR<=26' > ${target2c}.mat
    fi
    if [ $trilinear -eq 1 ]; then
	${FSLDIR}/bin/flirt -in $T -ref $T -applyxfm -init ${target2c}.mat -out ${target2c} 
    elif [ $sinc -eq 1 ]; then
	${FSLDIR}/bin/flirt -in $T -ref $T -applyxfm -init ${target2c}.mat -out ${target2c} \
	    -interp sinc
    else
	echo Interp not specified -- Defaulting to SINC interpolation!
	${FSLDIR}/bin/flirt -in $T -ref $T -applyxfm -init ${target2c}.mat -out ${target2c} \
	    -interp sinc
    fi
fi
echo "Generated target-to-mid-space transformation"

##############################################################################
# Transform all images to AV space
##############################################################################
midsp_images=${T}_to_midsp
for g in $@; do
    g=`${FSLDIR}/bin/remove_ext $g`
    totarget="`basename $g`_to_`basename $T`"
    if [ "$REG" != '-a' ]  && [ "$REG" != '-r' ]; then
	convertwarp --warp1=${totarget}_warp --warp2=${target2c}_warp -r $T -o ${g}_to_midsp_warp
	applywarp -i $g -r $T -w ${g}_to_midsp_warp -o ${g}_to_midsp
    else
	convert_xfm -omat ${g}_to_midsp.mat -concat ${target2c}.mat ${totarget}.mat 
	
	if [ $trilinear -eq 1 ]; then	
	    flirt -in $g -ref $T -applyxfm -init ${g}_to_midsp.mat -out ${g}_to_midsp 
	elif [ $sinc -eq 1 ]; then
	    flirt -in $g -ref $T -applyxfm -init ${g}_to_midsp.mat -out ${g}_to_midsp \
		-interp sinc
	else
	    echo Interp not specified -- Defaulting to SINC interpolation!
	    flirt -in $g -ref $T -applyxfm -init ${g}_to_midsp.mat -out ${g}_to_midsp \
		-interp sinc
	fi
    fi
    midsp_images="$midsp_images ${g}_to_midsp"	
done
echo "Applied transformations to images"

##############################################################################
# Final average
##############################################################################
if [ "$average" != "" ]; then
    ${FSLDIR}/bin/fslmaths `echo $midsp_images | sed 's/ / -add /g'` -div `expr $# + 1` $average
    
	###for f in $addwarps; do ${FSLDIR}/bin/imrm ${f%%_warp}; done
	###/bin/rm -f $addmats
    
    if [ `${FSLDIR}/bin/imtest $average` -eq 1 ]; then
	echo "Final image average \"${average}\""
    else
	echo "ERROR ($0): \"${average}\" was not generated." >&2; exit 1
    fi
    
fi
