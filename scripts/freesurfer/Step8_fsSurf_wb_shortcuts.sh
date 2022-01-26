#! /bin/sh

Subj=$1
dirFreesurfer=$2 #/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/
export SUBJECTS_DIR=$dirFreesurfer

/misc/data19/schonehr/ProControl/scripts/freesurfer/wb_shortcuts -freesurfer-resample-prep \
/misc/data19/schonehr/ProControl/data/DONE/${Subj}/surfaces/${Subj}/xhemi/surf/lh.white \
/misc/data19/schonehr/ProControl/data/DONE/${Subj}/surfaces/${Subj}/xhemi/surf/lh.pial \
/misc/data19/schonehr/ProControl/data/DONE/${Subj}/surfaces/${Subj}/xhemi/surf/lh.fsaverage_sym.sphere.reg \
/misc/data19/schonehr/ProControl/model/masks/Joern/rh.SPHERE.REG.surf.gii \
/misc/data19/schonehr/ProControl/data/DONE/${Subj}/surfaces/${Subj}/gifti/lh.xhemimidthickness.surf.gii \
/misc/data19/schonehr/ProControl/model/masks/Joern/rh.midthickness.surf.gii \
/misc/data19/schonehr/ProControl/data/DONE/${Subj}/surfaces/${Subj}/gifti/lh.xhemisphere.reg.surf.gii
