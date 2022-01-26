#! /bin/sh

dirFreesurfer=/vols/Data/soma/pre-post/surfaces/sub-aa03/
subject=sub-aa03
export SUBJECTS_DIR=$dirFreesurfer

/vols/Data/soma/pre-post/scripts/wb_shortcuts -freesurfer-resample-prep \
/vols/Data/soma/pre-post/surfaces/sub-aa03/sub-aa03/xhemi/surf/lh.white \
/vols/Data/soma/pre-post/surfaces/sub-aa03/sub-aa03/xhemi/surf/lh.pial \
/vols/Data/soma/pre-post/surfaces/sub-aa03/sub-aa03/xhemi/surf/lh.fsaverage_sym.sphere.reg \
/vols/Data/soma/Atlases/Joern/rh.sphere.reg.surf.gii \
/vols/Data/soma/pre-post/surfaces/sub-aa03/sub-aa03/gifti/lh.xhemimidthickness.surf.gii \
/vols/Data/soma/Atlases/Joern/R.midthickness.surf.gii \
/vols/Data/soma/pre-post/surfaces/sub-aa03/sub-aa03/gifti/lh.xhemisphere.reg.surf.gii
