#! /bin/sh

dirFreesurfer=/vols/Data/soma/pre-post/surfaces/
subject=sub-aa03
export SUBJECTS_DIR=$dirFreesurfer

wb_command -label-resample /vols/Data/soma/Atlases/Joern/ROI_J.label.gii \
/vols/Data/soma/Atlases/Joern/rh.SPHERE.REG.surf.gii \
/vols/Data/soma/pre-post/surfaces/sub-aa03/sub-aa03/gifti/lh.xhemisphere.reg.surf.gii ADAP_BARY_AREA \
/vols/Data/soma/pre-post/surfaces/sub-aa03/sub-aa03/gifti/ROI/sub-aa03.ROI.R.label.gii -area-surfs \
/vols/Data/soma/Atlases/Joern/rh.midthickness.surf.gii /vols/Data/soma/pre-post/surfaces/sub-aa03/sub-aa03/gifti/lh.xhemimidthickness.surf.gii
