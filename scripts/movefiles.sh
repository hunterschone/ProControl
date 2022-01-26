#!/bin/bash

subj=$1
sess=$2

cd /vols/Data/soma/superusers/ProControl/${subj}/${sess}/
mkdir anat func model model/glm model/masks model/glm/movieview model/glm/visloc model/glm/moveivew/run{1..6}_inmidsp.feat model/glm/movieview/run{1..6}_inmidsp.feat/stats
echo '-------------------------'
echo 'Copying Files'

mv /vols/Data/soma/superusers/ProControl/${subj}/${sess}/raw/dirs/MV1/*.nii.gz /vols/Data/soma/superusers/ProControl/${subj}/${sess}/func/${subj}_task_run-1.nii.gz;
mv /vols/Data/soma/superusers/ProControl/${subj}/${sess}/raw/dirs/MV2/*.nii.gz /vols/Data/soma/superusers/ProControl/${subj}/${sess}/func/${subj}_task_run-2.nii.gz;
mv /vols/Data/soma/superusers/ProControl/${subj}/${sess}/raw/dirs/MV3/*.nii.gz /vols/Data/soma/superusers/ProControl/${subj}/${sess}/func/${subj}_task_run-3.nii.gz;
mv /vols/Data/soma/superusers/ProControl/${subj}/${sess}/raw/dirs/MV4/*.nii.gz /vols/Data/soma/superusers/ProControl/${subj}/${sess}/func/${subj}_task_run-4.nii.gz;
mv /vols/Data/soma/superusers/ProControl/${subj}/${sess}/raw/dirs/MV5/*.nii.gz /vols/Data/soma/superusers/ProControl/${subj}/${sess}/func/${subj}_task_run-5.nii.gz;
mv /vols/Data/soma/superusers/ProControl/${subj}/${sess}/raw/dirs/MV6/*.nii.gz /vols/Data/soma/superusers/ProControl/${subj}/${sess}/func/${subj}_task_run-6.nii.gz;
mv /vols/Data/soma/superusers/ProControl/${subj}/${sess}/raw/dirs/HT/*.nii.gz /vols/Data/soma/superusers/ProControl/${subj}/${sess}/func/${subj}_task_hand-tool_localizer.nii.gz;
mv /vols/Data/soma/superusers/ProControl/${subj}/${sess}/raw/dirs/ANAT/*abcd.nii.gz /vols/Data/soma/superusers/ProControl/${subj}/${sess}/anat/${subj}_T1w.nii.gz

echo '-------------------------'

