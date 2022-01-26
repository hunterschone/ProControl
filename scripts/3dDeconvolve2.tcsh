#!/bin/tcsh -xef

#Set main pathways
set subdir=/misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/output
#Results Prefix
set results_prefix = ${subdir}/sub-ar01.EXP
#Move into directory for 3dDeconvolve
cd $subdir

3dDeconvolve  \
-polort A   \
-local_times \
-nodata 300 1.5 \
-xjpeg designEXP \
-x1D sub-ar01.EXP \
-num_stimts 21   \
-stim_times 1 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond_instructionx.txt 'SPMG2(1.5)' -stim_label 1 instruction \
-stim_times 2 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond0x.txt 'SPMG2(2)' -stim_label 2 move_open \
-stim_times 3 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond1x.txt 'SPMG2(2)' -stim_label 3 view_hand_open \
-stim_times 4 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond2x.txt 'SPMG2(2)' -stim_label 4 view_pros_open \
-stim_times 5 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond3x.txt 'SPMG2(2)' -stim_label 5 move_close \
-stim_times 6 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond4x.txt 'SPMG2(2)' -stim_label 6 view_hand_close \
-stim_times 7 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond5x.txt 'SPMG2(2)' -stim_label 7 view_pros_close \
-stim_times 8 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond6x.txt 'SPMG2(2)' -stim_label 8 move_pinch \
-stim_times 9 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond7x.txt 'SPMG2(2)' -stim_label 9 view_hand_pinch \
-stim_times 10 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond8x.txt 'SPMG2(2)' -stim_label 10 view_pros_pinch \
-stim_times 11 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond9x.txt 'SPMG2(2)' -stim_label 11 move_tripod \
-stim_times 12 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond10x.txt 'SPMG2(2)' -stim_label 12 view_hand_tripod \
-stim_times 13 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond11x.txt 'SPMG2(2)' -stim_label 13 view_pros_tripod \
-stim_times 14 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond12x.txt 'SPMG2(2)' -stim_label 14 move_1 \
-stim_times 15 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond13x.txt 'SPMG2(2)' -stim_label 15 view_hand_1 \
-stim_times 16 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond14x.txt 'SPMG2(2)' -stim_label 16 move_2 \
-stim_times 17 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond15x.txt 'SPMG2(2)' -stim_label 17 view_hand_2 \
-stim_times 18 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond16x.txt 'SPMG2(2)' -stim_label 18 move_3 \
-stim_times 19 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond17x.txt 'SPMG2(2)' -stim_label 19 view_hand_3 \
-stim_times 20 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond18x.txt 'SPMG2(2)' -stim_label 20 move_4 \
-stim_times 21 /misc/data19/schonehr/ProControl/data/sub-ar01/pre/model/onset_timings/final_run1/cond19x.txt 'SPMG2(2)' -stim_label 21 view_hand_4 \
-full_first -fout -tout \
-cbucket ${results_prefix}.stats.cbucket             \
-bucket ${results_prefix}.stats.bucket 


echo 'Done'


