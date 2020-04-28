#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from threading import Thread
from utils import display
from utils import var

cap = cv2.VideoCapture(0)
frame = np.zeros([240, 320, 3], np.uint8)
thread = Thread()

running = True

def updateframe():
    global frame
    r, f = cap.read()
    if r:
        frame = f
    display.updatebig(frame)
    k = display.show()
    exit = (k == 27)
    if k == ord('q'):
        display.clearsmall()
        display.clearText()
        var.savImg.dir_reset()
    return r and not exit

def loop():
    global running
    while running:
        running = updateframe()
    print('cam loop exit')
    cap.release()
    print('cam released')
    return

def start():
    global thread
    thread = Thread(target=loop)
    thread.start()
    return
