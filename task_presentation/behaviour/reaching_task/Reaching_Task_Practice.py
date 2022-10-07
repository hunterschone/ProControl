#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Wed Dec 16 15:04:50 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random
import copy

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'Reaching_Task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/slapuser/Desktop/ProControl/tasks/ReachingTask/Reaching_Task.py',
    savePickle=False,)
# save a log file for detail verbose info
endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
width = 1920
height = 1080
bottom = (-(1/2) * height + 100)

win = visual.Window(
    size=[width, height], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
    
introText = visual.TextStim(win, text = 'Welcome to the sLaP Reaching Task. \n \n Please ask your experimenter to press "space" when you are ready to begin', 
                                            units = 'pix', font='Arial', pos=(0, 0), height= 50, wrapWidth=None, ori=0, 
                                            color='white', colorSpace='rgb', opacity=1)
#store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

#Create Button component

buttonClock = core.Clock()
beginTrial = visual.ButtonStim(win, 
   text='', font='Arvo',
   pos=(0, bottom),units='pix',
   letterHeight=0.05,
   size=(20,20), borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='beginTrial')
beginTrial.buttonClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Home = visual.Rect(
    win=win, name='Home',units='pix', 
    width=(20,20)[0], height=(20,20)[1],
    ori=0, pos=(0, bottom),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[255, 0, 0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
#List of posistions
Possible_Positions = [[-640, -130], [0, 271], [640, -130]]
#Index through a copy to avoid destroying original list
Positions = copy.deepcopy(Possible_Positions)
Target = visual.Circle(
    win=win, name='Target', radius = 10, units='pix', 
    ori=0,
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[255,255,255], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
    
pointer = visual.TextStim(win, text = '+', color = 'lightgreen', height = 30)
cursor = visual.CustomMouse(win, visible = True, pointer = pointer)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10, method='random',  #Number of trials
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

trialNum = 0
for thisTrial in trials:
    cursor.mouse.setVisible(False)
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    if trialNum == 0: #If on title screen
        routineTimer.add(240.000)
        introText.draw()
        cursor.draw()
        win.flip()
        if event.waitKeys(keyList = 'space'):
            trialNum += 1
            thisExp.nextEntry()
        
    else:
        # ------Prepare to start Routine "button"-------
        continueRoutine = True
        routineTimer.add(100.100000)
        # update component parameters for each repeat
        beginTrial.setText('Tap')
        # keep track of which components have finished
        buttonComponents = [beginTrial]
        for thisComponent in buttonComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        buttonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "button"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = buttonClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=buttonClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *beginTrial* updates
            beginTrial.status = STARTED
            beginTrial.draw()
            cursor.draw()
            if beginTrial.status == STARTED:
                # check whether beginTrial has been pressed
                if beginTrial.isClicked:
                    if not beginTrial.wasClicked:
                        continueRoutine = False  # end routine when beginTrial is clicked
                        None
                    beginTrial.wasClicked = True  # if beginTrial is still clicked next frame, it is not a new click
                else:
                    beginTrial.wasClicked = False  # if beginTrial is clicked next frame, it is a new click
            else:
                beginTrial.wasClicked = False  # if beginTrial is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
    # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        cursor.draw()
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        Position = random.choice(Positions)
        Target.setPos(Position)
        Positions.remove(Position)
        if len(Positions) == 0:
            Positions = copy.deepcopy(Possible_Positions) #rebuild positions array to repeat again for n# cycles
            
        # keep track of which components have finished
        trialComponents = [Home, Target]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Home* updates
            if Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Home.frameNStart = frameN  # exact frame index
                Home.tStart = t  # local t and not account for scr refresh
                Home.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Home, 'tStartRefresh')  # time at next scr refresh
                Home.draw()
                cursor.draw()
                Home.status = STARTED
            if Home.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if t > 5.0:
                    # keep track of stop time/frame for later
                    Home.tStop = t  # not accounting for scr refresh
                    Home.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Home, 'tStopRefresh')  # time at next scr refresh
                    Home.status = FINISHED
            
            # *Target* updates
            if Target.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                Target.frameNStart = frameN  # exact frame index
                Target.tStart = t  # local t and not account for scr refresh
                Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
                Target.draw()
                cursor.draw()
                Target.status = STARTED
            if Target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if t > 5.0:
                    # keep track of stop time/frame for later
                    Target.tStop = t  # not accounting for scr refresh
                    Target.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Target, 'tStopRefresh')  # time at next scr refresh
                    Target.status = FINISHED
                    continueRoutine = False
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    Home.status = NOT_STARTED
                    Target.status = NOT_STARTED
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break

            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
                
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()