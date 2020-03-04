#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

######################################################
#size:(240, 320, 3) ->(1080,1440,3) / (960,1280,3)


roi = (0,100, 1920, 980)
arealimit = 50
lower_bounds = np.array([0, 0, 100])
upper_bounds = np.array([40, 40, 255])

######################################################


