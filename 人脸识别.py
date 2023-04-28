import cv2
import numpy as np

img = cv2.imread('./opencv_python_stu/faces.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
if img is None:
    print('img is none')
#人脸特征文件。下载地址为git里面github.com/opencv/opencv/tree/master/data/haarcascades
face_detector = cv2.CascadeClassifier('./opencv_python_stu/haarcascade_frontalface_alt.xml')
#faces =face_detector.detectMultiScale(gray)#坐标x,y.w.h
faces =face_detector.detectMultiScale(gray,scaleFactor=1.04,
                                      minNeighbors=3)#坐标x,y.w.h
for x,y,w,h in faces:
    cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=2) 
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindow()