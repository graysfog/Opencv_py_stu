import cv2
import numpy as np

def clamp(pv):
    if pv>255:
        return 255
    if pv<0:
        return 0
    else:
        return pv

def gaussion_noise(image):
    h,w,c=image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)
            b=image[row,col,0]
            g=image[row,col,1]
            r=image[row,col,2]
            image[row,col,0]=clamp(b+s[0])
            image[row,col,1]=clamp(g+s[1])
            image[row,col,2]=clamp(r+s[2])
    cv2.imshow('noise image',image)



g_srcImage =cv2.imread('opencv_python_stu\\face.jpg')
t1=cv2.getTickCount()
gaussion_noise(g_srcImage)
t2=cv2.getTickCount()
time=(t2-t1)/cv2.getTickFrequency()
print(time)

dst=cv2.GaussianBlur(g_srcImage,(0,0),15)
cv2.imshow("GaussianBlur",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()