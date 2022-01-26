Subj=$1 #sub-co01
dirSurf=$2 #/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/gifti
dirFreesurfer=$3 #/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01

  mkdir -p $dirSurf #make new folder, if not exists
  
  # convert orig and 001
  tkregister2 --mov $dirFreesurfer/mri/orig.mgz --targ $dirFreesurfer/mri/rawavg.mgz --regheader --reg junk --fslregout $dirSurf/freesurfer2struct.mat --noedit
  orig=$dirFreesurfer/mri/orig/001.mgz
  mri_convert $orig $dirSurf/orig.nii.gz
  conformed=$dirFreesurfer/mri/orig.mgz
  mri_convert $conformed $dirSurf/conformed.nii.gz

  for hemi in lh rh;do
    echo  Do hemisphere $hemi
    pial=$dirFreesurfer/surf/${hemi}.pial
    white=$dirFreesurfer/surf/${hemi}.white
    inflated=$dirFreesurfer/surf/${hemi}.inflated

    mris_convert $pial $dirSurf/${Subj}.${hemi}.pial.asc
    mris_convert $white $dirSurf/${Subj}.${hemi}.white.asc
    mris_convert $inflated $dirSurf/${Subj}.${hemi}.inflated.asc

    echo "addpath /misc/data19/schonehr/matlab/surfops" > $dirSurf/matscript.m
    echo "p=surfread('$dirSurf/${Subj}.${hemi}.pial.asc');" >> $dirSurf/matscript.m
    echo "w=surfread('$dirSurf/${Subj}.${hemi}.white.asc');" >> $dirSurf/matscript.m
    echo "p.vertices=.5*(p.vertices+w.vertices);" >> $dirSurf/matscript.m
    echo "surfwrite(p,'$dirSurf/${Subj}.${hemi}.midthickness.asc')" >> $dirSurf/matscript.m
    # This command creates the midthickness surface
    matlab -nodesktop -nosplash -r "run $dirSurf/matscript.m;quit;"

    #surf2surf - this will transform the surface into the original structural space
    for surf in pial white inflated midthickness;do
	     if [ ${hemi} == lh ];then
	       surf2surf -i $dirSurf/${Subj}.${hemi}.${surf}.asc -o $dirSurf/${Subj}.L.${surf}.surf.gii --convin=freesurfer --convout=caret --volin=$dirSurf/conformed --volout=$dirSurf/orig --xfm=$dirSurf/freesurfer2struct.mat
	       wb_command -set-structure $dirSurf/${Subj}.L.${surf}.surf.gii CORTEX_LEFT
       else
         surf2surf -i $dirSurf/${Subj}.${hemi}.${surf}.asc -o $dirSurf/${Subj}.R.${surf}.surf.gii --convin=freesurfer --convout=caret --volin=$dirSurf/conformed --volout=$dirSurf/orig --xfm=$dirSurf/freesurfer2struct.mat
         wb_command -set-structure $dirSurf/${Subj}.R.${surf}.surf.gii CORTEX_RIGHT
       fi
     done
   done

   #Retrieve curvature information
   hemi=lh
   curv=$dirFreesurfer/surf/${hemi}.curv
   surf=$dirFreesurfer/surf/${hemi}.white
   mris_convert -c $curv $surf $dirSurf/${Subj}.${hemi}.curv.func.gii
   wb_command -set-structure $dirSurf/${Subj}.${hemi}.curv.func.gii CORTEX_LEFT
   hemi=rh
   curv=$dirFreesurfer/surf/${hemi}.curv
   surf=$dirFreesurfer/surf/${hemi}.white
   mris_convert -c $curv $surf $dirSurf/${Subj}.${hemi}.curv.func.gii
   wb_command -set-structure $dirSurf/${Subj}.${hemi}.curv.func.gii CORTEX_RIGHT

   hemi=lh
   curv=$dirFreesurfer/surf/${hemi}.sulc
   surf=$dirFreesurfer/surf/${hemi}.white
   mris_convert -c $curv $surf $dirSurf/${Subj}.${hemi}.sulc.func.gii
   wb_command -set-structure $dirSurf/${Subj}.${hemi}.sulc.func.gii CORTEX_LEFT
   hemi=rh
   curv=$dirFreesurfer/surf/${hemi}.sulc
   surf=$dirFreesurfer/surf/${hemi}.white
   mris_convert -c $curv $surf $dirSurf/${Subj}.${hemi}.sulc.func.gii
   wb_command -set-structure $dirSurf/${Subj}.${hemi}.sulc.func.gii CORTEX_RIGHT
