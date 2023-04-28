import numpy as np
import cv2

image =cv2.imread('opencv_python_stu\\wugui.png')
image2=cv2.imread('opencv_python_stu\\face.jpg')
img2 = cv2.resize(image,(35,35))
img3 = np.repeat(img2,10,axis=0)
img4 = np.repeat(img3,10,axis=1)
cv2.imshow('masaike',img4)
image2[0:350,0:350]=img4
cv2.imshow('img',image2)
image[0:200,0:200] = img4[:200,:200]
cv2.imshow('image1',image)

#马赛克方式二
#img22=image[::10,::10] #每10个像素取出一个像素细节



cv2.waitKey(0)
cv2.destroyAllWindow()