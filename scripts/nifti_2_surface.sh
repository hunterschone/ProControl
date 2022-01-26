#!/bin/bash
#set -x
subj=$1
sess=$2

for side in L R; do
    surf_proj --data=/vols/Data/soma/superusers/ProControl/${subj}/${sess}/model/masks/OTC_top200/OTC_BOT_n20_visloc_top200_MNI.nii.gz --out=/vols/Data/soma/superusers/ProControl/${subj}/${sess}/model/masks/OTC_top200/OTC_BOT_n20_visloc_inmidsp.surf.${side}.func.gii --meshref=/vols/Data/soma/Atlases/HCP_Q1-2_GroupAvg_Related120_Unrelated40_v1/Q1-2_R120_AverageT1w_restore.nii.gz --surf=/vols/Data/soma/Atlases/HCP_Q1-2_GroupAvg_Related120_Unrelated40_v1/Q1-2_R120.${side}.inflated.32k_fs_LR.surf.gii --surfout --step=2;
done
