#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import var


b_size = [960, 1280, 3]
s_size = [480, 640, 3]
r_size = [b_size[0], b_size[1]+s_size[1], 3]


bimg = np.zeros(b_size, dtype=np.uint8)
simg = np.zeros(s_size, dtype=np.uint8)
rimg = np.zeros(r_size, dtype=np.uint8)


def resize(src, ratio):
    w, h, _ = src.shape
    w = int(w*ratio)
    h = int(h*ratio)
    return cv2.resize(src, (w, h))

def padTOP(src, px):
    px2add = px - src.shape[0]
    cv2.copyMakeBorder(x, px2add,0,0,0, cv2.BORDER_CONSTANT)
    return src

def padTOPtext(src, px, text):
    img = padTOP(src, px)
    #(影像, 文字, 座標, 
    # 字型, 大小, 
    # 顏色, 線條寬度, 線條種類)
    cv2.putText(img, text, (10, 10), 
                cv2.FONT_HERSHEY_DUPLEX,1, 
                (0, 0, 255), 1, cv2.LINE_AA)
    return img

def concat(big, small):
    small = padTOP(small, big.shape[0])
    return np.concatenate((big, small), axis=1)


