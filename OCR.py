import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("img/sample.png", cv2.IMREAD_COLOR)


grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binaryImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((7, 7), np.uint8)

dilationImg = cv2.dilate(binaryImg, kernel, iterations=1)

cv2.imshow('sample', dilationImg)
cv2.waitKey(0)

