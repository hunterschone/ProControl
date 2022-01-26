#! /bin/sh

dirFreesurfer=/misc/data19/schonehr/ProControl/data/DONE/sub-co02/surfaces/
subject=sub-co02
export SUBJECTS_DIR=$dirFreesurfer

mri_convert $dirFreesurfer/$subject/mri/T1.mgz $dirFreesurfer/$subject/mri/T1.nii.gz
