#实现图中找图
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 2.匹配多个物体
img_rgb = cv.imread('mario.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('mario_coin.jpg', 0)
h, w = template.shape[:2]

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
# 取匹配程度大于%80的坐标
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # *号表示可选参数
    bottom_right = (pt[0] + w, pt[1] + h)
    cv.rectangle(img_rgb, pt, bottom_right, (0, 0, 255), 2)

cv.imshow('img_rgb', img_rgb)
cv.waitKey(0)
cv.destroyAllWindows()
