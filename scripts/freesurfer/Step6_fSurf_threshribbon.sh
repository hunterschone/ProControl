#! /bin/bash

Subj=$1
dirSurf=$2 #/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/gifti/ROI/Volume

for side in 'lh'; do
	fslmaths $dirSurf/${Subj}.ROI_${side}_ribbon.nii.gz -thr 1.9 -uthr 2.1 -bin $dirSurf/${Subj}_${side}_M1_highres.nii.gz
	fslmaths $dirSurf/${Subj}.ROI_${side}_ribbon.nii.gz -thr .9 -uthr 1.1 -bin $dirSurf/${Subj}_${side}_S1_highres.nii.gz
	echo ${side}
done
