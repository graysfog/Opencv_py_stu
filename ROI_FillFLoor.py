import numpy as np
import cv2 as cv

src = cv.imread('opencv_python_stu\\wugui.png')
cv.imshow('src',src)
img =src[0:200,0:200]
cv.imshow('img',img)

mask = np.zeros([src.shape[0]+2,src.shape[1]+2,1],np.uint8)
cv.floodFill(src,mask,(10,10),(30,30,30),(30,30,30),cv.FLOODFILL_FIXED_RANGE)
cv.imshow('flood_fill',src)
cv.imshow('mask',mask)

cv.waitKey(0)
cv.destroyAllWindow()
