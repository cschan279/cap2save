#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

from utils import display
from utils import rfilter
from utils import cam
from utils import save
from utils import var

######################################################
#size:(240, 320, 3) ->(1080,1440,3) / (960,1280,3)
strformat='Last trigger: %d/%m/%y %H:%M:%S'

######################################################

if __name__ == "__main__":
    var.savImg = save.Saveimg()
    cam.start()
    while cam.running:
        trig, img = rfilter.checkimg(cam.frame)
        if trig:
            if not var.savImg.save_new(img):
                # new folder created
                display.updatesmall(img)
                display.updateText(save.timestamp(strformat=strformat))
        else:
            if var.savImg.dir_release():
                display.clearsmall()
                display.clearText()
    print('exit')
