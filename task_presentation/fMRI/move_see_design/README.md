# This directory has the fMRI stimuli, the fMRI task script and a script to construct the trialmatrix files used in the task
1. move_see design
    - Construct_trialmatrix.py - creates multiple iterations of the trialmatrix file which will be used as the input to run a single run of the task.
    - trialmat_rep3 - includes some example trial-matrix files I constructred using the construct_trialmatrix.py
    - Imaging_script.py - This is the move_see task script. I ran it in Pscychopy v.2021.1.1. Note: the uldaq directory and uldaq-packages are specific to the BIOPAC EMG device we were using during scanning. The idea was to have the task code to send triggers to the BIOPAC MP150 system during recording. If you are just testing the imaging_scripy.py code, make sure to comment out all uldaq related lines. If you are testing the code, you will be cued to input the subject code (anything), session (0,1), run number (any integer) and trialmat number (from what I added either 1,2,3: its looking for the trialmat_acceptable_option1.csv file in the trialmat directory)
    - uldaq directory - contains the packages I needed to send a trigger out via the python script. 
    - videos - this directory includes all of the biological and robotic hand videos I filmed. Additionally, the move cue is a expanding circle video I created using manim, see https://towardsdatascience.com/how-to-create-mathematical-animations-like-3blue1brown-using-python-f571fb9da3d1

