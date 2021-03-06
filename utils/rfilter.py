#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2

################################
arealimit = 250
lower_bounds = np.array([0, 0, 100])
upper_bounds = np.array([40, 40, 255])


roi = (0,100, 1920, 980) # x1, y1, x2, y2

draw = False

######################################################

def checkimg(img):
    global arealimit, lower_bounds, upper_bounds, draw, roi
    
    p_img = cv2.resize(img, (320, 240))
    #c_img = p_img[y1:y2, x1:x2]
    #mask = cv2.inRange(c_img, lower_bounds, upper_bounds)
    mask = cv2.inRange(p_img, lower_bounds, upper_bounds)
    _, contours,_ = cv2.findContours(mask, 
                                  cv2.RETR_EXTERNAL, 
                                  cv2.CHAIN_APPROX_SIMPLE)
    
    trig = False
    for c in contours:
        area = cv2.contourArea(c)
        if area >= arealimit:
            trig = True
            if draw:
                (x,y,w,h) = cv2.boundingRect(c)
                #x += roi[0]
                #y += roi[1]
                cv2.rectangle(p_img,(x,y),(x+w,y+h),(0,255,0),2)
    return trig, p_img

