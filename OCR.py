import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("img/sample.png", cv2.IMREAD_COLOR)
img1 = img.copy()

grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, binaryImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((13, 13), np.uint8)

dilationImg = cv2.dilate(binaryImg, kernel, iterations=1)

contours, hierachy = cv2.findContours(dilationImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
drawedImf = cv2.drawContours(binaryImg, contours, -1, (255, 255, 0), 2)
ticks = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    ticks.append((x, y, w, h))
    img1 = cv2.rectangle(img1,(x,y),(x+w, y+h),(0,255,0), 3)

print(ticks)

imgW = 600
imgH = 210

minWidth = 80

def addNucleus(ind):
    changeInd = ind
    x = 0
    for i in range(len(ticks)):
        if (not i == ind) and x < ticks[i][0] < ticks[ind][0]:
            changeInd = i
            x = ticks[i][0]
    mergeTick(changeInd, ind)


def mergeTick(ind1, ind2):
    mx = max(ticks[ind1][0], ticks[ind2][0])
    my = max(ticks[ind1][1], ticks[ind2][1])
    mw = max(ticks[ind1][0]+ticks[ind1][2], ticks[ind2][0]+ticks[ind2][2]) - mx
    mh = max(ticks[ind1][1]+ticks[ind1][3], ticks[ind2][1]+ticks[ind2][3]) - my

    ticks[ind1] = (mx, my, mw, mh)
    del ticks[ind2]

for i in range(len(ticks)):
    tick = ticks[i]
    if tick[0] + tick[2]/2 < minWidth:
        if tick[1] < imgH/3 :
            addNucleus(i)
    
for i in range(len(ticks)):
    for j in range(len(ticks)):
        if not i == j:
            
    
print(type(contours[0]))
cv2.imshow('sample', img1)
cv2.waitKey(0)

