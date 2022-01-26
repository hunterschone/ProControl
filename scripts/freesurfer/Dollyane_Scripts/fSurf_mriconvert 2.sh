#! /bin/sh

dirFreesurfer=/vols/Data/soma/pre-post/surfaces/sub-aa03/
subject=sub-aa03
export SUBJECTS_DIR=$dirFreesurfer

mri_convert $dirFreesurfer/$subject/mri/T1.mgz $dirFreesurfer/$subject/mri/T1.nii.gz
