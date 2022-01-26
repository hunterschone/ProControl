subj=$1
cd /vols/Data/soma/superusers/$subj/post1/raw/*/

for i in {2..24}; do
mkdir S${i};
tar -xf MQ?????_FIL.S${i}.tar -C S${i};
dcm2nii -o . S${i}/*;
done;
echo '-------------------------'
echo 'Done converting to nifti'

cd ../../
mkdir anat func fmap
echo '-------------------------'

echo 'Copying Files'
mv /vols/Data/soma/superusers/$subj/raw/*/*s002* /vols/Data/soma/superusers/$subj/func/${subj}_task-video_run-1_bold_ref.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s003* /vols/Data/soma/superusers/$subj/func/${subj}_task-video_run-1_bold.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s004* /vols/Data/soma/superusers/$subj/func/${subj}_task-video_run-2_bold_ref.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s005* /vols/Data/soma/superusers/$subj/func/${subj}_task-video_run-2_bold.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s006* /vols/Data/soma/superusers/$subj/func/${subj}_task-bodyloc_bold_ref.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s007* /vols/Data/soma/superusers/$subj/func/${subj}_task-bodyloc_bold.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s008* /vols/Data/soma/superusers/$subj/fmap/${subj}_magnitude.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s009* /vols/Data/soma/superusers/$subj/fmap/${subj}_phasediff.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/co*s010* /vols/Data/soma/superusers/$subj/anat/${subj}_T1w.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s011* /vols/Data/soma/superusers/$subj/func/${subj}_task-video_run-3_bold_ref.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s012* /vols/Data/soma/superusers/$subj/func/${subj}_task-video_run-3_bold.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s013* /vols/Data/soma/superusers/$subj/func/${subj}_task-visloc_bold_ref.nii.gz
mv /vols/Data/soma/superusers/$subj/raw/*/*s014* /vols/Data/soma/superusers/$subj/func/${subj}_task-visloc_bold.nii.gz

echo '-------------------------'
echo 'Deleting temp folders'
rm -rf /vols/Data/soma/superusers/$subj/post1/raw/*/S*
echo 'Finished deleting temp folders'

