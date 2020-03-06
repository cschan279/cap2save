#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import pyautogui as pyss
import time
import os.path
try:
    import winsound
except Exception as e:
    print('not in windows')


####################  Sound  #########################
#Set Sound freq and time

beep_freq = 1000 # Beep sound frequency in Hz
beep_duration = 800 # Beep sound duration in ms
######################################################
def alertsound():
    #print('\a') # for ubuntu
    try:
        winsound.Beep(beep_freq, beep_duration) # for window
    except Exception as e:
        pass
    return
######################################################
######################################################


####################  Config  ########################
######################################################
showcv = 0
showpop = True

# delay = fps * time in second
delay = 15

#roi equal to None for fullscreen capture
cv_X = 250
cv_Y = 200
cv_W = 1920-cv_X*2
cv_L = 1080-cv_Y 
roi = (cv_X, cv_Y, cv_W,cv_L)

# save_size equal to None/False for no resize
save_size = (cv_W//2,cv_L//2)
################################
popup_size = (cv_W//10,cv_L//10)
popup_loc = (100,100)
hold_time = 5
################################
arealimit = 250
lower_bounds = np.array([0, 0, 100])
upper_bounds = np.array([40, 40, 255])

######################################################
######################################################


##################  functions  #######################
######################################################
last_save = 0
def saveimg(fname, cvimg):
    global last_save, save_size
    current_time = time.time()
    if (current_time - last_save) <= 1:
        return False
    
    if save_size:
        cvimg = cv2.resize(cvimg, save_size, 
                           interpolation=cv2.INTER_AREA)
    cv2.imwrite(fname, cvimg)
    last_save = current_time
    return True

def timestamp():
    return time.strftime('%y%m%d_%H%M%S')

def newpath():
    pName = os.path.join('capture',timestamp())
    os.mkdir(pName)
    return pName

def newfilename(pathName):
    fn = timestamp()+'.png'
    return os.path.join(pathName, fn)

popimg = None
poptime = 0
def popupimg(newimg):
    global popimg, poptime
    poptime = time.time()
    if newimg is not None:
        print('new pop')
        cv2.namedWindow('popup',cv2.WINDOW_NORMAL)
        cv2.moveWindow('popup', *popup_loc)
        popimg = cv2.resize(newimg, save_size, 
                        interpolation=cv2.INTER_AREA)
    if popimg is not None:
        cv2.imshow('popup', popimg)
        k = cv2.waitKey(1)
        print('k', k)
        if not (k == -1 or k == 255):
            popimg = None
            cv2.destroyAllWindows()
    return

def closePopup():
    global poptime, hold_time
    if (time.time() - poptime) > hold_time:
        cv2.destroyAllWindows()
    return

folder_path = None
trigger_count = [False]*delay
def gen_fname(trigger, cvimg):
    global folder_path, trigger_count
    trigger_count.append(trigger)
    trigger_count.pop(0)
    #print(trigger_count)
    if any(trigger_count):
        alertsound() 
        if folder_path: 
            filename = newfilename(folder_path)
            popupimg(None)
            return filename # save in same folder
        else:
            folder_path = newpath()
            filename = newfilename(folder_path)
            popupimg(cvimg)
            return filename # save in new folder
    else:
        folder_path = None
        closePopup()
        return False
######################################################
######################################################

if showcv:
    cv2.namedWindow('screenshot',cv2.WINDOW_NORMAL)
t = 0

while True:
    ti = time.time()
    fps = int(1000/(ti - t))/1000
    print(fps, end='\r')
    t = ti
    imgss = pyss.screenshot(region=roi)
    img = cv2.cvtColor(np.array(imgss), cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(img, lower_bounds, upper_bounds)
    #cmask = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    trig = False
    for c in contours:
        area = cv2.contourArea(c)
        if area >= arealimit:
            trig = True
            if showcv:
                (x,y,w,h) = cv2.boundingRect(c)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    fname = gen_fname(trig, img)
     
    if fname:
        saveimg(fname, img)
    if showcv:
        cv2.imshow('thread', mask)
        cv2.imshow('screenshot', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
    
