#!/bin/bash

SUBJ=$1
WORKDIR="/misc/data19/schonehr/ProControl/scripts/freesurfer/"
COMMAND="fsRegisterXhem('${SUBJ}');"

matlab -nodisplay -nodesktop -nosplash -singleCompThread -r "cd '${WORKDIR}'; ${COMMAND}; quit;"


