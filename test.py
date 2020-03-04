#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2


x = cv2.imread('123.jpg')

x1 = cv2.copyMakeBorder(x, 200,0,0,0, cv2.BORDER_CONSTANT)

cv2.imshow('f', x1)
cv2.waitKey(0)
cv2.destroyAllWindows()
