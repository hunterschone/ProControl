### TRIAL-MATRIX WITH 20 UNIQUE CONDITIONS - 3 REPETITIONS
# =============================================================================
# BUILD A TRIAL DATAFRAME FOR ALL OF THE TRIALS 
# =============================================================================

from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy import core, tools, visual, monitors, sound, gui, event, colors, logging, clock, data
import os,random,sys,math,json,requests
from glob import glob
import pandas as pd
import numpy as np
import numpy.matlib
import csv
import parallel
from statistics import mean
import cv2

# DEFINE FILE PATH
path = os.getcwd()

# TIMING DURATIONS
tr = 1.5 # TR time
soa = 1.5 # time between the trial onsets
random_jitter = [x*1 for x in [1.5,3.0,4.5]]
random_jitter_probability = [.25,.50,.25]

# Define number of conditions
movesee =  [0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1] # move = 0, see = 1
grips = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,7,7] # 8 different gestures: 1=open, 2=close, 3=pinch, 4=1finger, 5=2fingers, 6=3fingers
stimuli = [0,1,2,0,1,2,0,1,2,0,1,2,0,1,0,1,0,1,0,1] # 0=circle video, 1=hand video, 2=pros video
ntrials= [20]
nstim = len(stimuli)

#Build trials -- I doubled n values, so its 3 repetitions of the 20 stimuli
column1 = np.matlib.repmat(np.repeat(movesee,1),1,1)
column2 = np.matlib.repmat(np.repeat(grips,1),1,1)
column3 = np.matlib.repmat(np.repeat(stimuli,1),1,1)

# #Little function to combine the condition values for the trialID column
def concat(a,b,c):
     return str(f"{a}{b}{c}")

trialmat = pd.DataFrame(column1[0],columns=['move_see'])
trialmat['grip']=(column2[0])
trialmat['stim']=(column3[0])
trialmat['trialID']=trialmat.apply(lambda row: concat(row.move_see,row.grip,row.stim),axis=1)
trialmat['uniquetrial'] = len(trialmat['trialID'])
ntrials = len(trialmat['trialID'])
trialmat['uniquetrial'] = range(20)

# #Create a grip_txt column that is filled with the values relating to the grip column
ms_conditions = [(trialmat['move_see'] == 0),(trialmat['move_see']== 1)]
moveseetxt = ['MOVE','VIEW']
trialmat['ms_txt'] = np.select(ms_conditions,moveseetxt)

# #Create a grip_txt column that is filled with the values relating to the grip column
grip_conditions = [(trialmat['grip'] == 0),(trialmat['grip']== 1),(trialmat['grip'] == 2),(trialmat['grip'] == 3),(trialmat['grip'] == 4),(trialmat['grip'] == 5),(trialmat['grip']== 6),(trialmat['grip']== 7)]
griptxt = ['OPEN','CLOSE','PINCH','TRIPOD','1 FINGER','2 FINGERS','3 FINGERS','4 FINGERS']
trialmat['grip_txt'] = np.select(grip_conditions,griptxt)

# Create a column that includes the DAQ output numbers: 1,2,4,8,16,32,64,128,255
daq = [(trialmat['move_see'] == 0) & (trialmat['grip_txt'] == 'OPEN'),(trialmat['move_see'] == 0) & (trialmat['grip_txt']== 'CLOSE'),(trialmat['move_see'] == 0) & (trialmat['grip_txt'] == 'PINCH'),(trialmat['move_see'] == 0) & (trialmat['grip_txt'] == 'TRIPOD'),(trialmat['move_see'] == 0) & (trialmat['grip_txt'] == '1 FINGER'),(trialmat['move_see'] == 0) & (trialmat['grip_txt'] == '2 FINGERS'),(trialmat['move_see'] == 0) & (trialmat['grip_txt']== '3 FINGERS'),(trialmat['move_see'] == 0) & (trialmat['grip_txt']== '4 FINGERS'),(trialmat['move_see'] == 1)]
daqtxt = ['1','2','4','8','16','32','64','128','255']
trialmat['daq'] = np.select(daq,daqtxt)

#Shuffle the rows 
trialmat = trialmat.sample(frac=1).reset_index(drop=True)
trialmat['trial_number']=range(ntrials) #so i don't need the index column

# #Create a jitter column
rand_jitter_lst = []
for t in range(ntrials):
    rand_jitter_lst.append(np.random.choice(a=random_jitter,p=random_jitter_probability))
trialmat['jitter']=(rand_jitter_lst)

#Check we've identified the correct number of stimuli
print('Video types:',nstim)
print('Number of unqiue videos:',len(sorted(glob('videos/*.mp4'))))
print('Number of gestures:',len(griptxt))
print('Number of total trials:',trialmat.shape[0])


# # =============================================================================
# # CREATE PRE-COMPUTED TRIALMAT FILES THAT DON'T REPEAT CODITIONS TOO MANY TIMES
# # =============================================================================

accept_min_repeatrate = [0,0]
accept_max_repeatrate = [0.25,0.05]

# # # ## I'M GOING TO MAKE 800 PRE-MADE TRIALMATS THAT I CAN USE, 200 IS ARBITRARY
idx = 0
for tries in range(800):
    for rep in range(3):
        dummy=1
        while dummy:
             idx = idx+1
             lst = []
             repeats = pd.DataFrame(np.nan, index=range(0,int(ntrials)), columns=['repeat_move_see','repeat_grip'])
             trialmat_random=trialmat.sample(frac=1,random_state=idx).reset_index(drop=True)
             # MOVE SEE
             repeats['repeat_move_see'] = trialmat_random.move_see.eq(trialmat_random.move_see.shift())
             #GRIP
             repeats['repeat_grip'] = trialmat_random.grip.eq(trialmat_random.grip.shift())
             columns = list(repeats) 


             for i in columns: 
                  lst.append(repeats[i].values.sum()/ntrials) 
             accept_repeatrate = []
             for i in range(len(lst)):
                 if (lst[i]>accept_min_repeatrate[i] and lst[i]<accept_max_repeatrate[i]):
                     accept_repeatrate.append(1)
                     print(lst[i])
                 else:
                     accept_repeatrate.append(0) 
                 if all(accept_repeatrate)==1:
                     trialmat_random.to_csv(index=False,path_or_buf=path+'/trialmat_rep3/raw/trialmat_acceptable_option' + str(tries+1) + '_rep' + str(rep) + '.csv')
                     dummy=0
    
    trialmat1 = pd.read_csv('./trialmat_rep3/raw/trialmat_acceptable_option' + str(tries+1) + '_rep0.csv')
    trialmat2 = pd.read_csv('./trialmat_rep3/raw/trialmat_acceptable_option' + str(tries+1) + '_rep1.csv')
    trialmat3 = pd.read_csv('./trialmat_rep3/raw/trialmat_acceptable_option' + str(tries+1) + '_rep2.csv')

    trialmats = [trialmat1, trialmat2]
    trialmat_v2 = pd.concat(trialmats)
    trialmats = [trialmat_v2, trialmat3]
    trialmat_final = pd.concat(trialmats)
    
     # # DEFINE THE TRIAL NUMBER COLUMN IN THE FINAL OUTPUT
    totaltrials = 60
    trialmat_final['trial_number']=range(totaltrials)
    trialmat_final.to_csv(index=False,path_or_buf=path+'/trialmat_rep3/final/trialmat_acceptable_option' + str(tries+1) + '.csv')  
    trialmat_final.to_csv(index=False,path_or_buf=path+'/trialmat_rep3/final/trialmat_acceptable_option' + str(tries+1) + '.csv') 