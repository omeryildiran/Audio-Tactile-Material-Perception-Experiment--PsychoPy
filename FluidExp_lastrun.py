#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on May 28, 2021, at 12:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'FluidExp'  # from the Builder filename that created this script
expInfo = {'participant': ''}
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
    originPath='C:\\Users\\omeru\\Documents\\FND\\My Repos\\Audio-Tactile Material Perception\\FluidExp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction1_1"
Instruction1_1Clock = core.Clock()
phase1instruction = visual.TextStim(win=win, name='phase1instruction',
    text='Hazır olup, ekrandaki butona dokunduktan sonra bir bip sesi duyacaksınız. Hemen ardından  yaklaşık 20sn boyunca bir nesneye dokunma sesleri duyacaksınız. İkinci bir bip sesi duyduktan sonra tekrar boşluk tuşuna basmanız ve bir sonraki ekranda çıkacak sıfatları dinlediğiniz seslerde hissettiklerinize göre değerlendirmeniz beklenmektedir',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
isReady = visual.TextStim(win=win, name='isReady',
    text='Hazırsanız başlamak için butona basınız',
    font='Open Sans',
    pos=(0, -0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
button = visual.ButtonStim(win, 
   text='        Başla', font='Open Sans',
   pos=(0, -0.4),
   letterHeight=0.05,
   size=[0.5,0.09], borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button')
button.buttonClock = core.Clock()

# Initialize components for Routine "beep"
beepClock = core.Clock()
BeepSound = sound.Sound('Sounds\\01_beep.wav', secs=0.3, stereo=True, hamming=True,
    name='BeepSound')
BeepSound.setVolume(1.0)
# Set experiment start values for variable component wait
wait = ''
waitContainer = []
sounnoised_2 = sound.Sound('noise.wav', secs=1.5, stereo=True, hamming=True,
    name='sounnoised_2')
sounnoised_2.setVolume(1.0)

# Initialize components for Routine "Stimuli_Presentation"
Stimuli_PresentationClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
audioNum=0

# Initialize components for Routine "beep_after"
beep_afterClock = core.Clock()
BeepSound_2 = sound.Sound('Sounds\\01_beep.wav', secs=0.3, stereo=True, hamming=True,
    name='BeepSound_2')
BeepSound_2.setVolume(1.0)
# Set experiment start values for variable component wait_2
wait_2 = ''
wait_2Container = []
sounnoised = sound.Sound('noise.wav', secs=1.5, stereo=True, hamming=True,
    name='sounnoised')
sounnoised.setVolume(1.0)

# Initialize components for Routine "Ratings"
RatingsClock = core.Clock()
def audioRatingfunc(i):
    vars()["adjective_"+str(i)]= visual.Slider(win=win, name="adjective_"+str(i),
    size=(1.28, 0.023), pos=(0, 0.466-(i*0.05)), units=None,
    labels=["0","25","50","75","100"], ticks=(0,25,50,75,100), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color=(1.0000, 0.9608, 0.9608), fillColor=(1.0000, -0.0039, -0.3725), borderColor=(0.8824, 1.0000, 1.0000), colorSpace='rgb',
    font='Open Sans', labelHeight=0.020,
    flip=False, depth=0, readOnly=False)
    return eval("adjective_"+str(i))
for i in range(12):
    vars()["adjective_"+str(i)]=audioRatingfunc(i)


# Initialize components for Routine "blank"
blankClock = core.Clock()
next_button = visual.ButtonStim(win, 
   text='        Devam', font='Open Sans',
   pos=(0, 0),
   letterHeight=0.05,
   size=[0.5,0.09], borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='next_button')
next_button.buttonClock = core.Clock()
sound_2 = sound.Sound('Sounds\\01_beep.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "end_message"
end_messageClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Deneyin tüm aşamalarını tamamladınız. Katılımınız için teşekkür ederiz\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_button = visual.ButtonStim(win, 
   text='        Bitir', font='Open Sans',
   pos=(0, 0),
   letterHeight=0.05,
   size=[0.5,0.09], borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='end_button')
end_button.buttonClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction1_1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Instruction1_1Components = [phase1instruction, key_resp, isReady, button]
for thisComponent in Instruction1_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction1_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction1_1"-------
while continueRoutine:
    # get current time
    t = Instruction1_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction1_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *phase1instruction* updates
    if phase1instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        phase1instruction.frameNStart = frameN  # exact frame index
        phase1instruction.tStart = t  # local t and not account for scr refresh
        phase1instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(phase1instruction, 'tStartRefresh')  # time at next scr refresh
        phase1instruction.setAutoDraw(True)
    
    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *isReady* updates
    if isReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        isReady.frameNStart = frameN  # exact frame index
        isReady.tStart = t  # local t and not account for scr refresh
        isReady.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(isReady, 'tStartRefresh')  # time at next scr refresh
        isReady.setAutoDraw(True)
    
    # *button* updates
    if button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
            else:
                button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = True  # if button is still clicked next frame, it is not a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button.wasClicked = False  # if button is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction1_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction1_1"-------
for thisComponent in Instruction1_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Instruction1_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SoundTrials = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Fluids.xlsx'),
    seed=None, name='SoundTrials')
thisExp.addLoop(SoundTrials)  # add the loop to the experiment
thisSoundTrial = SoundTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSoundTrial.rgb)
if thisSoundTrial != None:
    for paramName in thisSoundTrial:
        exec('{} = thisSoundTrial[paramName]'.format(paramName))

for thisSoundTrial in SoundTrials:
    currentLoop = SoundTrials
    # abbreviate parameter names if possible (e.g. rgb = thisSoundTrial.rgb)
    if thisSoundTrial != None:
        for paramName in thisSoundTrial:
            exec('{} = thisSoundTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "beep"-------
    continueRoutine = True
    routineTimer.add(1.800000)
    # update component parameters for each repeat
    BeepSound.setSound('Sounds\\01_beep.wav', secs=0.3, hamming=True)
    BeepSound.setVolume(1.0, log=False)
    sounnoised_2.setSound('noise.wav', secs=1.5, hamming=True)
    sounnoised_2.setVolume(1.0, log=False)
    # keep track of which components have finished
    beepComponents = [BeepSound, sounnoised_2]
    for thisComponent in beepComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    beepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "beep"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = beepClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=beepClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop BeepSound
        if BeepSound.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
            # keep track of start time/frame for later
            BeepSound.frameNStart = frameN  # exact frame index
            BeepSound.tStart = t  # local t and not account for scr refresh
            BeepSound.tStartRefresh = tThisFlipGlobal  # on global time
            BeepSound.play(when=win)  # sync with win flip
        if BeepSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BeepSound.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                BeepSound.tStop = t  # not accounting for scr refresh
                BeepSound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BeepSound, 'tStopRefresh')  # time at next scr refresh
                BeepSound.stop()
        # start/stop sounnoised_2
        if sounnoised_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sounnoised_2.frameNStart = frameN  # exact frame index
            sounnoised_2.tStart = t  # local t and not account for scr refresh
            sounnoised_2.tStartRefresh = tThisFlipGlobal  # on global time
            sounnoised_2.play(when=win)  # sync with win flip
        if sounnoised_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sounnoised_2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                sounnoised_2.tStop = t  # not accounting for scr refresh
                sounnoised_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sounnoised_2, 'tStopRefresh')  # time at next scr refresh
                sounnoised_2.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in beepComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "beep"-------
    for thisComponent in beepComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BeepSound.stop()  # ensure sound has stopped at end of routine
    SoundTrials.addData('BeepSound.started', BeepSound.tStartRefresh)
    SoundTrials.addData('BeepSound.stopped', BeepSound.tStopRefresh)
    sounnoised_2.stop()  # ensure sound has stopped at end of routine
    SoundTrials.addData('sounnoised_2.started', sounnoised_2.tStartRefresh)
    SoundTrials.addData('sounnoised_2.stopped', sounnoised_2.tStopRefresh)
    
    # ------Prepare to start Routine "Stimuli_Presentation"-------
    continueRoutine = True
    routineTimer.add(13.000000)
    # update component parameters for each repeat
    sound_1.setSound(soundsFile, secs=13.0, hamming=True)
    sound_1.setVolume(1.0, log=False)
    # keep track of which components have finished
    Stimuli_PresentationComponents = [sound_1]
    for thisComponent in Stimuli_PresentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Stimuli_PresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Stimuli_Presentation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Stimuli_PresentationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Stimuli_PresentationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 13.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stimuli_PresentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Stimuli_Presentation"-------
    for thisComponent in Stimuli_PresentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    SoundTrials.addData('sound_1.started', sound_1.tStartRefresh)
    SoundTrials.addData('sound_1.stopped', sound_1.tStopRefresh)
    
    # ------Prepare to start Routine "beep_after"-------
    continueRoutine = True
    routineTimer.add(1.900000)
    # update component parameters for each repeat
    BeepSound_2.setSound('Sounds\\01_beep.wav', secs=0.3, hamming=True)
    BeepSound_2.setVolume(1.0, log=False)
    sounnoised.setSound('noise.wav', secs=1.5, hamming=True)
    sounnoised.setVolume(1.0, log=False)
    # keep track of which components have finished
    beep_afterComponents = [BeepSound_2, sounnoised]
    for thisComponent in beep_afterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    beep_afterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "beep_after"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = beep_afterClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=beep_afterClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop BeepSound_2
        if BeepSound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BeepSound_2.frameNStart = frameN  # exact frame index
            BeepSound_2.tStart = t  # local t and not account for scr refresh
            BeepSound_2.tStartRefresh = tThisFlipGlobal  # on global time
            BeepSound_2.play(when=win)  # sync with win flip
        if BeepSound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BeepSound_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                BeepSound_2.tStop = t  # not accounting for scr refresh
                BeepSound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BeepSound_2, 'tStopRefresh')  # time at next scr refresh
                BeepSound_2.stop()
        # start/stop sounnoised
        if sounnoised.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            sounnoised.frameNStart = frameN  # exact frame index
            sounnoised.tStart = t  # local t and not account for scr refresh
            sounnoised.tStartRefresh = tThisFlipGlobal  # on global time
            sounnoised.play(when=win)  # sync with win flip
        if sounnoised.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sounnoised.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                sounnoised.tStop = t  # not accounting for scr refresh
                sounnoised.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sounnoised, 'tStopRefresh')  # time at next scr refresh
                sounnoised.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in beep_afterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "beep_after"-------
    for thisComponent in beep_afterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BeepSound_2.stop()  # ensure sound has stopped at end of routine
    SoundTrials.addData('BeepSound_2.started', BeepSound_2.tStartRefresh)
    SoundTrials.addData('BeepSound_2.stopped', BeepSound_2.tStopRefresh)
    sounnoised.stop()  # ensure sound has stopped at end of routine
    SoundTrials.addData('sounnoised.started', sounnoised.tStartRefresh)
    SoundTrials.addData('sounnoised.stopped', sounnoised.tStopRefresh)
    
    # ------Prepare to start Routine "Ratings"-------
    continueRoutine = True
    # update component parameters for each repeat
    b=randint(0,12)
    posListe=list(range(12))
    shuffle(posListe)
    Adj=[]
    for x in range(12):
        k=posListe[x]
        eval("adjective_"+str(x)).reset()
        Adj.append(eval("adjective_"+str(x)))
        eval("adjective_"+str(x)).pos=(0,0.458-(k*0.082))
    
    for thisComponent in Adj:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # keep track of which components have finished
    RatingsComponents = []
    for thisComponent in RatingsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RatingsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Ratings"-------
    while continueRoutine:
        # get current time
        t = RatingsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RatingsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        rightAdjList=['Cıvık','Jölemsi','Sümüksü','Yapışkan','Nemli','Kaygan','Havadar','Kabarık','Süngerimsi','Pürüzlü','Sıcak','Pahalı']
        for i in range(12):
            #k=(i+b)%10
            k=posListe[i]
            
            rightText = visual.TextStim(win=win, name=rightAdjList[i],
                text=rightAdjList[i],
                font='Open Sans',
                pos=(0.760, 0.4549-(k*0.0817)), height=0.0212, wrapWidth=None, ori=0.0, 
                color='white', colorSpace='rgb', opacity=None, 
                languageStyle='LTR',
                depth=-5.0);
           
            if rightText.status == NOT_STARTED:
                rightText.draw()
        
        RatingsComponents=Adj
        for i in range(12):
            if eval("adjective_"+str(i)).status==NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eval("adjective_"+str(i)).frameNStart = frameN  # exact frame index
                eval("adjective_"+str(i)).tStart = t  # local t and not account for scr refresh
                eval("adjective_"+str(i)).tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eval("adjective_"+str(i)), 'tStartRefresh')  # time at next scr refresh
                eval("adjective_"+str(i)).setAutoDraw(True)
        
        if adjective_0.getRating() is not None and  adjective_1.getRating() is not None and  adjective_2.getRating() is not None and  adjective_3.getRating() is not None and  adjective_4.getRating() is not None and  adjective_5.getRating() is not None and  adjective_6.getRating() is not None and  adjective_7.getRating() is not None and  adjective_8.getRating() is not None and  adjective_9.getRating() is not None and  adjective_10.getRating() is not None and  adjective_11.getRating() is not None:
                continueRoutine = False
                
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RatingsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ratings"-------
    for thisComponent in RatingsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    for i in range(12):
        vars()["adjective_"+str(i)]
        SoundTrials.addData('adjective_'+str(i)+'.response',eval("adjective_"+str(i)).getRating())
    for thisComponent in Adj:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
            
    
    # the Routine "Ratings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_2.setSound('Sounds\\01_beep.wav', secs=1.0, hamming=True)
    sound_2.setVolume(1.0, log=False)
    # keep track of which components have finished
    blankComponents = [next_button, sound_2]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *next_button* updates
        if next_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_button.frameNStart = frameN  # exact frame index
            next_button.tStart = t  # local t and not account for scr refresh
            next_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_button, 'tStartRefresh')  # time at next scr refresh
            next_button.setAutoDraw(True)
        if next_button.status == STARTED:
            # check whether next_button has been pressed
            if next_button.isClicked:
                if not next_button.wasClicked:
                    next_button.timesOn.append(next_button.buttonClock.getTime()) # store time of first click
                    next_button.timesOff.append(next_button.buttonClock.getTime()) # store time clicked until
                else:
                    next_button.timesOff[-1] = next_button.buttonClock.getTime() # update time clicked until
                if not next_button.wasClicked:
                    continueRoutine = False  # end routine when next_button is clicked
                    None
                next_button.wasClicked = True  # if next_button is still clicked next frame, it is not a new click
            else:
                next_button.wasClicked = False  # if next_button is clicked next frame, it is a new click
        else:
            next_button.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
            next_button.wasClicked = False  # if next_button is clicked next frame, it is a new click
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop()  # ensure sound has stopped at end of routine
    SoundTrials.addData('sound_2.started', sound_2.tStartRefresh)
    SoundTrials.addData('sound_2.stopped', sound_2.tStopRefresh)
    # the Routine "blank" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'SoundTrials'


# ------Prepare to start Routine "end_message"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
end_messageComponents = [end_text, end_button]
for thisComponent in end_messageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_messageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_message"-------
while continueRoutine:
    # get current time
    t = end_messageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_messageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
    # *end_button* updates
    if end_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_button.frameNStart = frameN  # exact frame index
        end_button.tStart = t  # local t and not account for scr refresh
        end_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_button, 'tStartRefresh')  # time at next scr refresh
        end_button.setAutoDraw(True)
    if end_button.status == STARTED:
        # check whether end_button has been pressed
        if end_button.isClicked:
            if not end_button.wasClicked:
                end_button.timesOn.append(end_button.buttonClock.getTime()) # store time of first click
                end_button.timesOff.append(end_button.buttonClock.getTime()) # store time clicked until
            else:
                end_button.timesOff[-1] = end_button.buttonClock.getTime() # update time clicked until
            if not end_button.wasClicked:
                continueRoutine = False  # end routine when end_button is clicked
                None
            end_button.wasClicked = True  # if end_button is still clicked next frame, it is not a new click
        else:
            end_button.wasClicked = False  # if end_button is clicked next frame, it is a new click
    else:
        end_button.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        end_button.wasClicked = False  # if end_button is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_messageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_message"-------
for thisComponent in end_messageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)
# the Routine "end_message" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
