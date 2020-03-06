#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np


cv2.namedWindow("Thermo", cv2.WINDOW_NORMAL)


r_size = [1060, 1920, 3]
rimg = np.zeros(r_size, np.uint8)

bw, bh = 1280, 960
sw, sh = 640,480
#480:640
#bg[480:1080, 1100:1900] = rect

def updatesmall(src):
    global sh, sw, r_size, rimg
    img = cv2.resize(src, (sw, sh))
    x1 = r_size[0] - sh
    x2 = r_size[0]
    y1 = r_size[1] - sw
    y2 = r_size[1]
    rimg[x1:x2, y1:y2] = img
    return

def clearsmall():
    global sh, sw, r_size, rimg
    img = np.zeros([sh, sw, 3], np.uint8)
    x1 = r_size[0] - sh
    x2 = r_size[0]
    y1 = r_size[1] - sw
    y2 = r_size[1]
    rimg[x1:x2, y1:y2] = img
    return
    
def updatebig(src):
    global bh, bw, r_size, rimg
    img = cv2.resize(src, (bw, bh))
    rimg[0:bh, 0:bw] = img
    return

def updateText(txt):
    global r_size, rimg, bw
    w = r_size[1] - bw
    h = 200
    cover = np.zeros([h, w, 3], np.uint8)
    #(影像, 文字, 座標, 
    # 字型, 大小, 
    # 顏色, 線條寬度, 線條種類)
    cv2.putText(cover, txt, (10, 30), 
                cv2.FONT_HERSHEY_DUPLEX,1, 
                (0, 0, 255), 1, cv2.LINE_AA)
    rimg[0:h, bw:r_size[1]] = cover
    return

def clearText():
    global r_size, rimg, bw
    w = r_size[1] - bw
    h = 200
    cover = np.zeros([h, w, 3], np.uint8)
    rimg[0:h, bw:r_size[1]] = cover
    return

def show():
    global rimg
    img = rimg.copy()
    cv2.imshow("Thermo", img)
    k = cv2.waitKey(1) & 0xFF
    return k
