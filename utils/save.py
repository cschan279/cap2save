#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import var
import cv2
import os.path
import time

class Saveimg:
    def __init__(self):
        self.base_dir = 'capture'
        self.save_dir = None
        
        self.save_gap = 1
        self.lastsave = 0
        
    def save_query(self, img):
        pass
    
    
    def save(img):
        cv2.imsave
