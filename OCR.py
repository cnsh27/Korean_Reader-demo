import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("img/sample.png", cv2.IMREAD_COLOR)
img1 = img.copy()

grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, binaryImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((7, 7), np.uint8)

dilationImg = cv2.dilate(binaryImg, kernel, iterations=1)

contours, hierachy = cv2.findContours(dilationImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
drawedImf = cv2.drawContours(binaryImg, contours, -1, (255, 255, 0), 2)
xticks = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    xticks.append()
    img1 = cv2.rectangle(img1,(x,y),(x+w, y+h),(0,255,0), 3)

cv2.imshow('sample', img1)
cv2.waitKey(0)

