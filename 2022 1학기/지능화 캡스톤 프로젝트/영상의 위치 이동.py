# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:18:32 2022

@author: User
"""

import cv2
import numpy as np
img=cv2.imread('lena.bmp')
height,width=img.shape[:2]
M=np.float32([[1,0,50],[0,1,100]])
img2=cv2.warpAffine(img,M,(width,height))
cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
