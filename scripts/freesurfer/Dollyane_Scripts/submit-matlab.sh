#!/bin/bash

(( $# < 1 )) && echoerrx1 "Usage: $0 <TaskFile>"
TASK=$1
QUEUE=$2
PROJECT=$3
WAIT=$4

# make sure file exists
[ ! -f "$TASK" ] && echoerrx1 "Task file not found: $1"

# check if the job should wait for any previous one
if [ $# -eq 4 ]; then
	matID=$(fsl_sub -q "$QUEUE" -N "$PROJECT" -t "$TASK" -j "$WAIT") 
else
	matID=$(fsl_sub -q "$QUEUE" -N "$PROJECT" -t "$TASK")
fi

echo $matID

