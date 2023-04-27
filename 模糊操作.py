#均值模糊
#中值模糊
#自定义模糊
import cv2
import numpy as np

def blur_demo(img):
    dst=cv2.blur(img,(1,3))
    cv2.imshow('dst',dst)

def media_blur_demo(img):
    dst=cv2.medianBlur(img,5)
    cv2.imshow('dst',dst)

def custom_blur_demo(img):
    kernel=np.ones([5,5],np.float32)/25
    #kernel=np.array([[0,-1,-],[-,5,-1],[1,1,1]],np.float32)/9
    dst=cv2.filter2D(img,-1,kernel=kernel)
    cv2.imshow('showWindow',dst)

g_srcImage =cv2.imread('opencv_python_stu\\face.jpg')

#cv2.namedWindow('showWindow',cv2.WINDOW_AUTOSIZE)
custom_blur_demo(g_srcImage)


cv2.waitKey(0)
cv2.destroyAllWindows()