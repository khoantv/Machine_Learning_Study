"""
Goal
Learn to:
    Access pixel values and modify them
    Access image properties
    Set a Region of Interest (ROI)
    Split and merge images
"""

import numpy as np
import cv2 as cv

img = cv.imread(r'..\images\cat1.jpg')
px = img[100, 100]  # truy cập theo tọa độ pixel
print(px)
blue = img[100,100,0]  # truy cập theo mãu
print(px)

# modifying RED value
img.itemset((10,10,2), 100)
# accessing RED value

img.item(10,10,2)




