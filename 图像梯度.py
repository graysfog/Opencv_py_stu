import cv2
import numpy as np

def sobel_demo(img):
    grad_x = cv2.Sobel(img,cv2.CV_32F,1,0)
    grad_y=cv2.Sobel(img,cv2.CV_32F,0,1)
    gradx=cv2.convertScaleAbs(grad_x)
    grady=cv2.convertScaleAbs(grad_y)
    cv2.imshow('gradient_x',gradx)
    cv2.imshow('gradient_y',grady)
    gradxy = cv2.addWeighted(gradx,0.5,grady,0.5,0)
    cv2.imshow('gradient',gradxy)

def Scharr_demo(img):
    grad_x = cv2.Scharr(img,cv2.CV_32F,1,0)
    grad_y = cv2.Scharr(img,cv2.CV_32F,0,1)
    gradx = cv2.convertScaleAbs(grad_x)
    grady=cv2.convertScaleAbs(grad_y)
    cv2.imshow('gradient_x',gradx)
    cv2.imshow('gradient_y',grady)
    gradxy=cv2.addWeighted(gradx,0.5,grady,0.5,0)
    cv2.imshow('gradxy',gradxy)


src = cv2.imread('./opencv_python_stu/wugui.png')
cv2.namedWindow('input_img',cv2.WINDOW_NORMAL)
cv2.imshow('input_img',src)
Scharr_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
