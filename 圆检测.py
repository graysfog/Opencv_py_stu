import cv2
import numpy as np

img = cv2.imread('./opencv_python_stu/circle.png')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.medianBlur(gray_img,5)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=35,minRadius=0,maxRadius=0)
#对数据进行四舍五入变为整数
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    #画出来圆的边界
    cv2.circle(img,(i[0],i[1]),i[2],(0,0,0),2)
    #画出来圆心
    cv2.circle(img,(i[0],i[1]),2,(0,255,255),3)
cv2.imshow("Circle",img)
cv2.waitKey()
cv2.destroyAllWindows()

