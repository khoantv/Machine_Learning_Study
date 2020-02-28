import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load a color image in grayscale
img = cv.imread(r'..\images\cat1.jpg', cv.IMREAD_COLOR)
bgr_img2 = cv.cvtColor(img, cv.COLOR_RGB2BGR)
plt.imshow(bgr_img2)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


