import cv2 as cv
import numpy as np

#对象测量
def measure_object(image):
    #灰度图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value : %s"%ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    #轮廓检测
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        #求取轮廓的面积
        area = cv.contourArea(contour)
        #得到轮廓的外接矩形
        x, y, w, h = cv.boundingRect(contour)
        #求出宽高比
        rate = min(w, h)/max(w, h)
        print("rectangle rate : %s"%rate)
        #求取几何矩
        mm = cv.moments(contour)
        print(type(mm)) #mm:字典类型
        #得到中心位置
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        #绘制圆
        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        #对每个轮廓绘制外接矩形
        #cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("contour area %s"%area)
        #多边形逼近，  True：表示闭合
        approxCurve = cv.approxPolyDP(contour,4, True)
        print(approxCurve.shape)
        if approxCurve.shape[0] > 6:
            #画在二值化图像上
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)
        if approxCurve.shape[0] == 4:
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)
        if approxCurve.shape[0] == 3:
            cv.drawContours(dst, contours, i, (255, 0, 0), 2)
        if approxCurve.shape[0] == 6:
            cv.drawContours(dst, contours, i, (100, 0, 100), 2)    
    cv.imshow("measure-contours", dst)


print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("D:/vcprojects/images/blob.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
measure_object(src)
cv.waitKey(0)

cv.destroyAllWindows()
