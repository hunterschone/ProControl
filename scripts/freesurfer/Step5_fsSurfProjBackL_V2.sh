labelmetric=L #use this function for label files, i.e. data that is discrete/categorical e.g. ROIs
#fsl_sub -q veryshort.q sh fsSurfProjBackL.sh sub-aa02 /vols/Data/soma/pre-post/surfaces/sub-aa02/gifti/ 1 /vols/Data/soma/pre-post/surfaces/sub-aa02/gifti/ROI/sub-aa02.ROI.R.label.gii
Subj=$1
dirSurf=$2 #/vols/Data/soma/6Finger/surf/SF1/gifti/
xhem=0; # 0 (L) or 1 (R)
dataInput=$3 #/vols/Data/soma/6Finger/surf/SF1/gifti/ROI/SF1.ROI.L.label.gii

surfpialL=$dirSurf/${Subj}.L.pial.surf.gii
surfwhiteL=$dirSurf/${Subj}.L.white.surf.gii

volume=$dirSurf/orig.nii.gz
#tmp=${dataInput##*/};
#output=$dirSurf/Volume/${tmp%%.$side*}

mkdir -p $dirSurf/Volume
wb_command -label-to-volume-mapping $dataInput $surfpialL $volume ${dirSurf}/Volume/${Subj}.ROI_lh_ribbon.nii.gz -ribbon-constrained $surfwhiteL $surfpialL
