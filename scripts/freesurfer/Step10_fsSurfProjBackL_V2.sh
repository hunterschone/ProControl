#labelmetric=L #use this function for label files, i.e. data that is discrete/categorical e.g. ROIs
#fsl_sub -q veryshort.q sh fsSurfProjBackL.sh sub-aa02 /vols/Data/soma/pre-post/surfaces/sub-aa02/gifti 1 /vols/Data/soma/pre-post/surfaces/sub-aa02/gifti/ROI/sub-aa02.ROI.R.label.gii
Subj=$1
dirSurf=$2 #/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/gifti
xhem=1; # 0 (L) or 1 (R)
dataInput=$3 #/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/gifti/ROI/sub-co01.ROI.R.label.gii

surfpialR=$dirSurf/${Subj}.R.pial.surf.gii
surfwhiteR=$dirSurf/${Subj}.R.white.surf.gii

volume=$dirSurf/orig.nii.gz

mkdir -p $dirSurf/Volume
wb_command -label-to-volume-mapping $dataInput $surfpialR $volume ${dirSurf}/Volume/${Subj}.ROI_rh_ribbon.nii.gz -ribbon-constrained $surfwhiteR $surfpialR

