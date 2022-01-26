#! /bin/bash

cd /vols/Data/soma/superusers
for subj in 'sub-co01'; do
	cp ${subj}/model/masks/top100hemi/LOTC_L_midtrans.nii.gz /vols/Data/soma/superusers/masks/final_OTC_subj_masks/
	mv /vols/Data/soma/superusers/masks/final_OTC_subj_masks/LOTC_L_midtrans.nii.gz /vols/Data/soma/superusers/masks/final_OTC_subj_masks/${subj}_L_OTC.nii.gz
	cp ${subj}/model/masks/top100hemi/LOTC_R_midtrans.nii.gz /vols/Data/soma/superusers/masks/final_OTC_subj_masks/
	mv /vols/Data/soma/superusers/masks/final_OTC_subj_masks/LOTC_R_midtrans.nii.gz /vols/Data/soma/superusers/masks/final_OTC_subj_masks/${subj}_R_OTC.nii.gz
done; 
