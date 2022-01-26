#! /bin/sh

cd /misc/data19/schonehr/ProControl/data/DONE/

mkdir -p /misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces
dirFreesurfer=/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces
export SUBJECTS_DIR=$dirFreesurfer
fsl_sub -q verylong.q recon-all -s sub-co01 -i /misc/data19/schonehr/ProControl/data/DONE/sub-co01/pre/anat/sub-co01_T1w.nii.gz -all
