#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2

################################
arealimit = 250
lower_bounds = np.array([0, 0, 100])
upper_bounds = np.array([40, 40, 255])

######################################################

def checkimg(img):
    global arealimit, lower_bounds, upper_bounds
    
    mask = cv2.inRange(img, lower_bounds, upper_bounds)
    contours,_ = cv2.findContours(mask, 
                                  cv2.RETR_EXTERNAL, 
                                  cv2.CHAIN_APPROX_SIMPLE)
    
    trig = False
    for c in contours:
        area = cv2.contourArea(c)
        if area >= arealimit:
            trig = True
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return trig, img

