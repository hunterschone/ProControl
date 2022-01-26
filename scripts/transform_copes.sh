#!/bin/bash
subj=$1
sess=$2

echo $subj
echo $sess

cd /vols/Data/soma/superusers/ProControl/

for run in {1..6}; do
    for i in {1..24}; do
        fsl_sub -q veryshort.q flirt -ref ${subj}/${sess}/func/Midtrans -in ${subj}/${sess}/model/glm/moveview/run${run}_v2.feat/stats/cope${i}.nii.gz -applyxfm -init ${subj}/${sess}/func/*run-${run}_ref_to_midsp.mat -out ${subj}/${sess}/model/glm/moveview/run${run}_v2_inmidsp.feat/stats/cope${i}.nii.gz -nosearch
    done;
    fsl_sub -q veryshort.q flirt -ref ${subj}/${sess}/func/Midtrans -in ${subj}/${sess}/model/glm/moveview/run${run}_v2.feat/stats/res4d.nii.gz -applyxfm -init ${subj}/${sess}/func/*run-${run}_ref_to_midsp.mat -out ${subj}/${sess}/model/glm/moveview/run${run}_v2_inmidsp.feat/stats/res4d.nii.gz -nosearch
done;




