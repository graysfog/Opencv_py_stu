import cv2 
import numpy as np

def nothing():
    pass
g_srcImage =cv2.imread('opencv_python_stu\\wugui.png')
g_srcImage_copy = g_srcImage.copy()
cv2.cvtColor(g_srcImage_copy,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('xiaoguotu')
cv2.createTrackbar('fuchazuidazhi','xiaoguotu',0,255,nothing)
cv2.createTrackbar('zhengchazuidazhi','xiaoguotu',0,255,nothing)

cv2.imshow('xiaoguotu',g_srcImage_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()