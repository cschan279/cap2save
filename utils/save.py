#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import var
import cv2
import os.path
import time

def timestamp(pattern='{}'):
    return pattern.format(time.strftime('%y%m%d_%H%M%S'))


class Saveimg:
    def __init__(self):
        self.base_dir = 'capture'
        self.save_dir = None
        
        self.save_gap = 1
        self.lastsave = 0
        
        return
    
    


    def save_query(self, img):
        pass
    
    
    def save(img):
        
        try:
            fname = os.path.join(self.save_dir, timestamp('{}.jpg'))
            cv2.imsave(fname, img)
        except Exception as e:
            print(e)
