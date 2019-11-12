#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:09:37 2019

@author: benedictpark
"""

## This is pseudocode for my counter-strike experiment ##
# In this experiment, we want to see how people track a moving object with
# a mouse. The goal of this experiment is to create a novel, more informative
# continuous performance task (CPT).
# In this task, participants are instructed to track a moving target on a
# screen using their mouse.
# Thus, we operationalize ATTENTION = (ability to track a quickly accelerating
# object - ability to track a slowly accelerating object).
# RQ: Does acceleration of target influence tracking performance over time?
# IV1: Low direction change (ctrl) vs. med/high/insane direction change (exp) 
# of a target.
# IV2: Low acceleration change (ctrl) vs. med/high/insane acceleration change
# (exp) of a target.
# DV1: Distance of mouse from target at every time point during each trial.
# Predicted utilities to use: Psychopy/Pygame.

import os
import shutil
import numpy as np
import scipy as sp
import pandas as pd
import pygame
import psychopy

# Import stuff.
# Get computer info.
# Ask for subject info.
# Create screen.
win= psychopy.visual.Window(size=[400,400],fullscr=False,color=[20,20,20],units="pix")
text_start= psychopy.visual.TextStim(win=win,text='hello world',color=[-1,-1,-1])
text_start.pos= [20,20]
text_start.draw()
win.flip()
psychopy.event.waitKeys()
win.close()

# Set up experimental parameters (blocktype, trialtype).
    # durations: ITI, stim-cue, post-cue(rdm), track(rdm), RI, points.
    # numblocks: 10.
    # blocktypes: 
    # trialtypes: 
        # Accel Rate: low accel, med accel, high accel, nsane accel.
        # Heading Change Rate: low hdrate, med hdrate, high hdrate, nsane hdrate.
    # numtrialsperblock: 60.
    # randomize/counterbalance controlled variables.
# Start experiment.
    # Per block:
        # Ready? Spacebar to continue.
        # Per trial:
            # Randomize trial variables (durations, start heading).
            # Present ITI.
            # Present stim-cue.
            # Present post-cue.
            # Present track (start accelerate + headingch).
                # Randomize heading change amount by hdrate.
                # Randomize acceleration change amount by accelrate.
                # Record mouse movement per t.
                # Record participant rt to track onset (t to hit target first time).
                # Record mouse distance from targetcenter per t.
                # Depending on distance from targetcenter, calculate points.
            # Present RI.
            # Present points feedback.
            # Save trial parameters, participant responses.
#End experiment.
#Save files.