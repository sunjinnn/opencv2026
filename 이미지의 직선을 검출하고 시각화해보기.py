#6.2 실습+cv.HoughLinesP() 추가
import cv2 as cv
import numpy as np
import math

img=cv.imread('soccer.jpg')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges=cv.Canny(gray, 100, 200) #에지 검출

height, width = edges.shape
diag_len = int(np.ceil(np.sqrt(width**2 + height**2)))

#허프 누산기 초기화
accumulator = np.zeros((2*diag_len, 180), dtype=np.uint64)

#좌표 순회하여 에지 픽셀이면 누산
y_idxs, x_idxs = np.nonzero(edges)
for i in range(len(x_idxs)):
    x = x_idxs[i]
    y = y_idxs[i]
    for theta in range(180):
        t=np.deg2rad(theta)
        rho=int(round(x*np.cos(t)+y*np.sin(t))+diag_len)
        accumulator[rho, theta] += 1
        
#누산기 시각화용 이미지 생성
acc_norm=cv.normalize(accumulator, None, 0, 255, cv.NORM_MINMAX)
acc_uint8=np.uint8(acc_norm)
acc_invert=cv.bitwise_not(acc_uint8)
acc_resize=cv.resize(acc_invert, (360, 240))

#결과출력
cv.imshow('Original', gray)
cv.imshow('Edges', edges)
cv.imshow('Hough Space (theto, rho', acc_resize)

cv.waitKey()
cv.destroyAllWindows()



