#! /bin/bash

dirSurf=$1 #/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/gifti
dataInput=$1 #/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces/sub-co01/gifti/ROI/sub-co01.ROI.L.label.gii

volume=$dirSurf/orig.nii.gz;
tmp=${dataInput%%.l*}; 
echo $tmp;
side=${tmp##*.};
echo $side;