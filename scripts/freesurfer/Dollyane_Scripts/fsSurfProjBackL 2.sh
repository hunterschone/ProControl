labelmetric=L #use this function for label files, i.e. data that is discrete/categorical e.g. ROIs

Subj=$1
dirSurf=$2 #/vols/Data/soma/6Finger/surf/SF1/gifti/
xhem=$3; # 0 (L) or 1 (R)
dataInput=$4 #/vols/Data/soma/6Finger/surf/SF1/gifti/ROI/SF1.ROI.L.label.gii
dataOutput=$5

surfDir=/vols/Data/soma/Adapticity/data/freesurfer

surfpialL=$dirSurf/${Subj}.L.pial.surf.gii
surfpialR=$dirSurf/${Subj}.R.pial.surf.gii
surfwhiteL=$dirSurf/${Subj}.L.white.surf.gii
surfwhiteR=$dirSurf/${Subj}.R.white.surf.gii

volume=$dirSurf/orig.nii.gz
tmp=${dataInput%%.l*}; side=${tmp##*.};
#tmp=${dataInput##*/};
#output=$dirSurf/Volume/${tmp%%.$side*}


mkdir -p $dirSurf/Volume

    if [ $side = L ]; then
      wb_command -label-to-volume-mapping $dataInput $surfpialL $volume ${dirSurf}/Volume/${Subj}_${dataOutput}.ROI_lh_ribbon.nii.gz -ribbon-constrained $surfwhiteL $surfpialL

    elif [ $side = R ]; then 
      wb_command -label-to-volume-mapping $dataInput $surfpialR $volume ${dirSurf}/Volume/${Subj}_${dataOutput}.ROI_rh_ribbon.nii.gz -ribbon-constrained $surfwhiteR $surfpialR

    fi

