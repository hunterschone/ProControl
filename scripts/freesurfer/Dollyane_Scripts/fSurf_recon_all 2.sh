#! /bin/sh
module load freesurfer
#need to mkdirr the subject folder
dirFreesurfer=/vols/Data/soma/pre-post/surfaces/sub-aa03/
subject=sub-aa03
export SUBJECTS_DIR=$dirFreesurfer
fsl_sub -q verylong.q recon-all -s sub-aa03 -i /vols/Data/soma/pre-post/sub-aa03/pre1/anat/sub-aa03_T1w.nii.gz -all

