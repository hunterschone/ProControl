#!/bin/bash

cd /vols/Data/soma/superusers/ProControl/sub-ar03/pre/
mkdir anat func model
echo '-------------------------'

echo 'Copying Files'
mv /vols/Data/soma/superusers/ProControl/sub-ar03/pre/raw/S9/*.nii.gz /vols/Data/soma/superusers/ProControl/sub-ar03/pre/func/sub-ar03_task_run-1.nii.gz;
mv /vols/Data/soma/superusers/ProControl/sub-ar03/pre/raw/S10/*.nii.gz /vols/Data/soma/superusers/ProControl/sub-ar03/pre/func/sub-ar03_task_run-2.nii.gz;
mv /vols/Data/soma/superusers/ProControl/sub-ar03/pre/raw/S11/*.nii.gz /vols/Data/soma/superusers/ProControl/sub-ar03/pre/func/sub-ar03_task_run-3.nii.gz;
mv /vols/Data/soma/superusers/ProControl/sub-ar03/pre/raw/S12/*.nii.gz /vols/Data/soma/superusers/ProControl/sub-ar03/pre/func/sub-ar03_task_run-4.nii.gz;
mv /vols/Data/soma/superusers/ProControl/sub-ar03/pre/raw/S13/*.nii.gz /vols/Data/soma/superusers/ProControl/sub-ar03/pre/func/sub-ar03_task_run-5.nii.gz;
mv /vols/Data/soma/superusers/ProControl/sub-ar03/pre/raw/S14/*.nii.gz /vols/Data/soma/superusers/ProControl/sub-ar03/pre/func/sub-ar03_task_run-6.nii.gz;
mv /vols/Data/soma/superusers/ProControl/sub-ar03/pre/raw/S15/*.nii.gz /vols/Data/soma/superusers/ProControl/sub-ar03/pre/func/sub-ar03_task_hand-tool_localizer.nii.gz;
mv /vols/Data/soma/superusers/ProControl/sub-ar03/pre/raw/S3/*.nii.gz /vols/Data/soma/superusers/ProControl/sub-ar03/pre/anat/sub-ar03_T1w.nii.gz

echo '-------------------------'

