#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import var
import cv2
import os
import time

def timestamp(pattern='{}'):
    return pattern.format(time.strftime('%y-%m-%d_%H-%M-%S'))


class Saveimg:
    def __init__(self):
        self.base_dir = 'capture'
        self.save_dir = None
        
        self.hold_gap = 5
        self.save_gap = 1
        self.lastsave = 0
        
        return
    
    
    def dir_release(self):
        if (time.time() - self.lastsave) >= self.hold_gap:
            self.save_dir = None
            return True
        else:
            return False

    def save_new(self, img):
        if self.save_dir:
            if timecount():
                self.save(img)
                return True
        else:
            self.save_dir = os.path.join(self.base_dir, timestamp())
            os.mkdir(self.save_dir)
            self.save(img)
            return False
    
    def timecount(self):
        t = time.time()
        if (t - self.lastsave) >= self.save_gap:
            return True
        else:
            return False
    
    def save(img):
        try:
            fname = os.path.join(self.save_dir, timestamp('{}.jpg'))
            cv2.imsave(fname, img)
            self.lastsave = time.time()
        except Exception as e:
            print(e)
