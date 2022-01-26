#!/usr/bin/python

import glob
import os
import sys
from optparse import OptionParser

parser = OptionParser(description="Checks for motion outliers")
parser.add_option("-s", "--subj", dest="subj", action="store", metavar="SUBJ")
    
(options, args) = parser.parse_args()

path = '/vols/Data/soma/superusers/%s'%(options.subj)
bold_files = glob.glob('%s/pre/func/%s_task_run-[1-6]_bold.nii.gz'%(path, options.subj))

for cur_bold in list(bold_files):
    print(cur_bold)
    # Store directory name
    cur_dir = os.path.dirname(cur_bold)

    # strip off .nii.gz from file name (makes code below easier)
    cur_bold_name = cur_bold[-13:-7]

    # Assessing motion.
    if os.path.isdir("%s/motion_assess/"%(cur_dir))==False:
      os.system("mkdir %s/motion_assess"%(cur_dir))
    os.system("fsl_motion_outliers -i %s -o %s/motion_assess/confound_%s.txt --fd --thresh=0.9 -p %s/motion_assess/fd_plot_%s -v > %s/motion_assess/outlier_output_%s.txt"%(cur_bold, cur_dir, cur_bold_name, cur_dir, cur_bold_name, cur_dir, cur_bold_name))

    # Last, if we're planning on modeling out scrubbed volumes later
    #   it is helpful to create an empty file if confound.txt isn't
    #   generated (i.e. no scrubbing needed).  It is basically a
    #   place holder to make future scripting easier
    if os.path.isfile("%s/motion_assess/confound_%s.txt"%(cur_dir, cur_bold_name))==False:
      os.system("touch %s/motion_assess/confound_%s.txt"%(cur_dir, cur_bold_name))




