#! /bin/bash

Subj=$1
target=1;

export SUBJECTS_DIR=/misc/data19/schonehr/ProControl/data/DONE/${Subj}/surfaces

surfreg --s ${Subj} --t fsaverage_sym --lh
xhemireg --s ${Subj}
surfreg --s ${Subj} --t fsaverage_sym --lh --xhemi
