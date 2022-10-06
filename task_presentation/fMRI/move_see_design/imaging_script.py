#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Hunter R. Schone, 2021

# =============================================================================
# IMPORTS
# =============================================================================
from __future__ import print_function
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy import core, tools, visual, monitors, sound, gui, event, colors, logging, clock, data
import os,random,sys,math,json,requests
from glob import glob
import pandas as pd
import numpy as np
import parallel
from statistics import mean
import cv2
from time import sleep
from os import system
from sys import stdout
from uldaq import (get_daq_device_inventory, DaqDevice, InterfaceType, DigitalDirection, DigitalPortIoType)
#comment out all uldaq if not connected to a BIOPAC MP150

# =============================================================================
# TASK PARAMETERS
# =============================================================================
# DEFINE FILE PATH
path = os.getcwd()
# KEYS
trigger_key = 't' 
space_key = 'space'
quit_button = 'q'
# TTIMING DURATIONS
tr = 1.5 # TR 
pre_fixation_time = 8*tr 
post_fixation_time = 6*tr 
refreshrate = 1/60 #needed to define to fix small timing offset when presenting the frames

# =============================================================================
# EMG - TRIGGER PARAMETERS - ONLY IF USING BIOPAC MP150, OTHERWISE COMMENT OUT
# =============================================================================

#Parameters before loop
daq_device = None
dio_device = None
port_to_write = None
port_info = None
interface_type = InterfaceType.ANY
port_types_index = 0
off_data=0
#Finding DAQ device and making connection
devices = get_daq_device_inventory(interface_type)
daq_device = DaqDevice(devices[0])
dio_device = daq_device.get_dio_device()
descriptor = daq_device.get_descriptor()
daq_device.connect(connection_code=0)
dio_info = dio_device.get_info()
port_types = dio_info.get_port_types()
if port_types_index >= len(port_types):
    port_types_index = len(port_types) - 1
port_to_write = port_types[port_types_index]
port_info = dio_info.get_port_info(port_to_write)
# Configure the port for output.
if (port_info.port_io_type == DigitalPortIoType.IO or
        port_info.port_io_type == DigitalPortIoType.BITIO):
    dio_device.d_config_port(port_to_write, DigitalDirection.OUTPUT)
system('clear')
max_port_value = int(pow(2.0, port_info.number_of_bits) - 1)

# =============================================================================
# SUBJECT INFO - EXPERIMENTER WILL BE PROMPTED TO MANUALLY ENTER THESE BEFORE TASK BEGINS
# the only one that needs to be specific is script number - it's looking for a trialmatrix file with the number you input
# =============================================================================
isrealexperiment = 1
if isrealexperiment==1:
    subject = {'Subject number':''}
    if not gui.DlgFromDict(subject,title='Enter subject info:').OK:
        print('User hit cancel at subject information')
        exit()
    try:
        a = str(subject['Subject number'])
    except:
        raise
    sess = {'Session':''}
    if not gui.DlgFromDict(sess,title='Enter the session:').OK:
        print('User hit cancel at run information')
        exit()
    try:
        b = str(sess['Session'])
    except:
        raise
    run = {'Run number':''}
    if not gui.DlgFromDict(run,title='Enter the run number:').OK:
        print('User hit cancel at run information')
        exit()
    try:
        c = int(run['Run number'])
    except:
        raise
    script = {'Script number':''}
    if not gui.DlgFromDict(script,title='Enter the script number:').OK:
        print('User hit cancel at run information')
        exit()
    try:
        d = int(script['Script number'])
    except:
        raise
# Store info about the experiment session
psychopyVersion = '2021.1.1'
expName = 'fmri_v2.py'
expInfo = {'': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
# This is how the format the data will be saved, create a data directory to save into
filename = path + os.sep + 'data' + os.sep + str(a) + '_sess_' + str(b) + '_run_' + str(c) + '_script_' + str(d)
# I opted to use an experiment handler to help with creating the timing file
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    saveWideText=True,dataFileName=filename)

# =============================================================================
# LOAD A PRE-COMPUTED TRIALMAT
# =============================================================================   
trialmat = pd.read_csv("./trialmat_rep3/final/trialmat_acceptable_option" + str(d) + ".csv")
def concat(a,b,c):
    return str(f"{a}{b}{c}")
trialmat['trialID']=trialmat.apply(lambda row: concat(row.move_see,row.grip,row.stim),axis=1)
trials = trialmat.index

# =============================================================================
# START TASK
# =============================================================================
# SETUP WINDOW
win = visual.Window(size=[1680, 1050], screen=0, fullscr=True, monitor='testMonitor', color=[0,0,0], colorSpace='rgb', units='pix')
# HIDE MOUSE DURING TASK
win.mouseVisible=False

# =============================================================================
# BUILD ALL VISUAL OBJECTS
# =============================================================================
pre_fixation = visual.TextStim(win=win, text="+",pos=(0,0),color='black',height = 75)
trial_fixation = visual.TextStim(win=win, text="+",pos=(0,0),color='black',height = 75)
grip_text = visual.TextStim(win=win, name='grip_text',text='',font='Open Sans',pos=(0, -150), height=125,color='white',wrapWidth=5000)
ms_text = visual.TextStim(win=win, name='ms_text',text='',font='Open Sans',pos=(0, 125), height=175,color='lawngreen',wrapWidth=5000)
jitter = visual.TextStim(win=win, text="+",pos=(0,0),color='black',height = 75)
post_fixation = visual.TextStim(win=win, text="+",pos=(0,0),color='black',height = 75)

# Build 1 list of movies based on index
movies1 = []
for p in range(20):
        movies1.append(visual.MovieStim3(win=win, name='movie',noAudio = False,filename=("./videos/20_cond/" + str(p) + ".mp4"),ori=0.0, pos=(0,0), opacity=1.0,loop=False,size=(1920,1080),depth=0.0))

welcome_trig_text = visual.TextStim(win,text='Welcome to the experiment!',pos=(0,0),height=75,wrapWidth=5000)
welcome_trig_text.draw()
welcome_trig_text = win.flip()
while 1:
        pressed=event.getKeys(keyList=space_key, modifiers=False, timeStamped=False) 
        if pressed:
            win.flip()
            break

# =============================================================================
# WAITING FOR SCANNER TRIGGER
# =============================================================================
scanner_trig_text = visual.TextStim(win,text='Waiting for scanner...',pos=(0,0),height=75,wrapWidth=5000)
scanner_trig_text.draw()
scanner_trig_text = win.flip()

dio_device.d_out(port_to_write, int(off_data)) #comment out if not using BIOPAC

while 1:
        pressed=event.getKeys(keyList=trigger_key, modifiers=False, timeStamped=False) 
        if pressed:
            pre_fixation.draw()
            win.flip()
            trialClock = core.MonotonicClock()
            break
core.wait(secs=(pre_fixation_time))

# =============================================================================
# LOOP THROUGH TRIALS
# =============================================================================
for i in trials:
        #currentLoop = trials
        keys_quit = event.getKeys(keyList=quit_button)
        if keys_quit:
            print('User hit quit button')
            win.close()
            core.quit()  

        # =============================================================================
        # PRE-TRIAL FIXATION
        # =============================================================================
        trial_fixation_started = trialClock.getTime()
        #Present trial fixation
        trial_fixation.draw()
        win.flip()
        core.wait(secs=(1.5-refreshrate)) # subtract half a frame from tthis
        #Output pre-trial fixation start-time  
        thisExp.addData('trial_fixation.started', trial_fixation_started)

        # =============================================================================
        # MOVE-SEE AND GRIP INSTRUCTION
        # =============================================================================
        #Modify the visual object within the loop
        grip_text.text = str(trialmat['grip_txt'][i])
        ms_text.text = str(trialmat['ms_txt'][i])
        #Setup timing components for grip_text
        grip_text_started = trialClock.getTime()
        #Present instruction
        grip_text.draw()
        trial_fixation.draw()
        ms_text.draw()
        win.flip()
        core.wait(secs=(1.0-refreshrate))  
        #Output instruction start-time
        thisExp.addData('instruction.started', grip_text_started)
        
        #Send trigger signal to BIOPAC AcqKnowledge - I made the triggers differ depending on the type of move trial
        on_data = str(trialmat['daq'][i]) 
        dio_device.d_out(port_to_write, int(on_data)) #comment out if not using BIOPAC
        
        #Present trial fixation
        trial_fixation.draw()
        win.flip()
        core.wait(secs=(.5)) 
        # =============================================================================
        # PLAY MOVIE
        # =============================================================================                
        #Setup timing components for mov
        mov_started = trialClock.getTime()
        #Output movie start-time
        thisExp.addData('mov.started', mov_started)
        
        #Present movie
        if i <= 19:
            for Nframes in range(116): 
                movies1[trialmat['uniquetrial'].iloc[i]].play()
                movies1[trialmat['uniquetrial'].iloc[i]].draw()
                win.flip()
            #Reset movie frames for future repeats
            movies1[trialmat['uniquetrial'].iloc[i]].seek(0)
        elif 20 <= i <= 39:
            for Nframes in range(116): #CHECK THIS PLAY BY FRAME APPROACH
                movies1[trialmat['uniquetrial'].iloc[i]].play()
                movies1[trialmat['uniquetrial'].iloc[i]].draw()
                win.flip()
            #Reset movie frames for future repeats
            movies1[trialmat['uniquetrial'].iloc[i]].seek(0)
        else:
            for Nframes in range(116): #CHECK THIS PLAY BY FRAME APPROACH
                movies1[trialmat['uniquetrial'].iloc[i]].play()
                movies1[trialmat['uniquetrial'].iloc[i]].draw()
                win.flip()
            #Reset movie frames for future repeats
            movies1[trialmat['uniquetrial'].iloc[i]].seek(0)
        
        #Turn off trigger (i.e. move trial is over)
        dio_device.d_out(port_to_write, int(off_data)) #comment out if not using BIOPAC

        # =============================================================================
        # JITTER
        # =============================================================================            
        #Setup timing components for mov
        jitter_started = trialClock.getTime()
        #Output jitter start-time
        thisExp.addData('jitter.started', jitter_started)
        #Present Jitter
        jitter.draw()
        win.flip()
        core.wait(secs=(trialmat['jitter'][i]-refreshrate))
        #Output subj,sess,run,script into timingmat
        thisExp.addData('subj', str(a))
        thisExp.addData('sess', str(b))
        thisExp.addData('run', str(c))
        thisExp.addData('script', str(d))
        #In the timing output file, this will move it to the next line
        thisExp.nextEntry()

# =============================================================================
# POST-FIXATION
# =============================================================================
#Present post-fixation
post_fixation.draw()
win.flip()
core.wait(secs=post_fixation_time)

# =============================================================================
# SAVE TIMINGMAT
# =============================================================================
thisExp.saveAsWideText(filename+'.csv', delim='comma')

# =============================================================================
# CONCAT TRIALMAT (INPUT) AND TIMINGMAT (BUILT DURING TASK) TOGETHER FOR A SINGLE OUTPUT
# =============================================================================
trialmat = pd.read_csv("./trialmat_rep3/final/trialmat_acceptable_option" + str(d) + ".csv")
timingmat = pd.read_csv("./data" + os.sep + str(a) + "_sess_" + str(b) + "_run_" + str(c) + "_script_" + str(d) + ".csv")
output_df = pd.concat([trialmat,timingmat], axis=1).reindex(trialmat.index)
output_df.to_csv("./output" + os.sep + str(a) + "_sess_" + str(b) + "_run_" + str(c) + "_script_" + str(d) + ".csv")

# =============================================================================
# CLOSE EVERYTHING
# =============================================================================
thisExp.abort()
win.close()
core.quit()