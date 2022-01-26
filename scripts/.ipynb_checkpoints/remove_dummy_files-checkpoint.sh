#!/bin/bash
cd /vols/Data/soma/superusers/ProControl
subjs=$1
sess=$2
for sub in $subjs; do
            cd ${sub}/${sess}/func/
            echo ${sub}
            fslroi ${sub}_task_run-1.nii.gz ${sub}_task_run-1_ref.nii.gz 4 5
            fslroi ${sub}_task_run-2.nii.gz ${sub}_task_run-2_ref.nii.gz 4 5
            fslroi ${sub}_task_run-3.nii.gz ${sub}_task_run-3_ref.nii.gz 4 5
            fslroi ${sub}_task_run-4.nii.gz ${sub}_task_run-4_ref.nii.gz 4 5
            fslroi ${sub}_task_run-5.nii.gz ${sub}_task_run-5_ref.nii.gz 4 5
            fslroi ${sub}_task_run-6.nii.gz ${sub}_task_run-6_ref.nii.gz 4 5
            fslroi ${sub}_task_hand-tool_localizer.nii.gz ${sub}_task_hand-tool_localizer_ref.nii.gz 4 5
done
echo "All done!"

