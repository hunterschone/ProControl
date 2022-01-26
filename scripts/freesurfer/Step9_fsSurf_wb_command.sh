#! /bin/sh

Subj=$1
dirFreesurfer=$2 #/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/
export SUBJECTS_DIR=$dirFreesurfer

wb_command -label-resample /misc/data19/schonehr/ProControl/model/masks/Joern/ROI_J.label.gii \
/misc/data19/schonehr/ProControl/model/masks/Joern/rh.SPHERE.REG.surf.gii \
/misc/data19/schonehr/ProControl/data/DONE/${Subj}/surfaces/${Subj}/gifti/lh.xhemisphere.reg.surf.gii ADAP_BARY_AREA \
/misc/data19/schonehr/ProControl/data/DONE/${Subj}/surfaces/${Subj}/gifti/ROI/${Subj}.ROI.R.label.gii -area-surfs \
/misc/data19/schonehr/ProControl/model/masks/Joern/rh.midthickness.surf.gii /misc/data19/schonehr/ProControl/data/DONE/${Subj}/surfaces/${Subj}/gifti/lh.xhemimidthickness.surf.gii
