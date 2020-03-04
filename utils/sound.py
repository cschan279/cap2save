#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
if os.name != 'posix':
    import winsound
else:
    print('running on posix system')

    

####################  Sound  #########################
#Set Sound freq and time

beep_freq = 1000 # Beep sound frequency in Hz
beep_duration = 800 # Beep sound duration in ms
######################################################
def alertsound()
    if os.name != 'posix':
        winsound.Beep(beep_freq, beep_duration) # for window
    else:
        print('\a') # for ubuntu
    return
######################################################
