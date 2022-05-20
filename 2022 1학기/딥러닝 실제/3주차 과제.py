# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:57:05 2022

@author: User
"""

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('전일우.jpg')

plt.imshow(img)
plt.show()