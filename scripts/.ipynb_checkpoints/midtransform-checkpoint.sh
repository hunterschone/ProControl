#!/bin/bash

subj=$1
sess=$2

cd /vols/Data/soma/superusers/ProControl/${subj}/${sess}/func
fsl_sub -q veryshort.q sh /misc/data19/schonehr/ProControl/scripts/midtransform_agt.sh -r -o Midtrans ${subj}_task_run-?_ref.nii.gz

echo "All done!"

