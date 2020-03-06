#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np


from utils import rfilter
from utils import cam
######################################################
#size:(240, 320, 3) ->(1080,1440,3) / (960,1280,3)


######################################################

if __name__ == "__main__":
    cam.start()
    while cam.running:
        trig, img = rfliter(cam.frame)
        if trig:
            
