# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:52:33 2022

@author: User
"""

import cv2
import numpy as np
img=cv2.imread('lena.bmp')
img1=cv2.flip(img,0)
img2=cv2.flip(img,1)
img3=cv2.flip(img,-1)
assert img is not None
cv2.imshow('img',img)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()