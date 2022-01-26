#!/bin/bash
#path=`pwd`
#cd $path

mask_name=$1
convert_file=/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/gifti/Volume/${mask_name}.nii.gz
out_file=/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/gifti/Volume/${mask_name}_MNI.nii.gz

flirt -in ${convert_file} -ref /misc/data19/schonehr/ProControl/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz -applyxfm -init \
	/misc/data19/schonehr/ProControl/data/DONE/sub-co01/pre/model/glm/moveview/run1.feat/reg/highres2standard.mat -out ${out_file} -interp nearestneighbour;
