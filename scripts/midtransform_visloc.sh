#!/bin/bash
cd /vols/Data/soma/superusers/sub-aa03/
fsl_sub -q veryshort.q midtransform_agt.sh -r -o Midtrans anat/sub-aa02_T1w.nii.gz anat/sub-aa02_T1w.nii.gz post2/anat/sub-aa02_T1w.nii.gz 

echo "All done!"
