#5.12
import cv2 as cv

img=cv.imread('soccer.jpg')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

grad_x=cv.Sobel(gray, cv.CV_32F,1,0,ksize=3) #소벨 연산자 적용
grad_y=cv.Sobel(gray, cv.CV_32F,0,1,ksize=3) #소벨 연산자는 미분을 1번밖에 안 함
 
sobel_x=cv.convertScaleAbs(grad_x)  #절댓값을 취해 양수 영상으로 변환
sobel_y=cv.convertScaleAbs(grad_y)

edge_strength=cv.addWeighted(sobel_x, 0.1, sobel_y, 0.1, 0) #에지 강도 계산

cv.imshow('Original', gray)
cv.imshow('sobel_x', sobel_x)
cv.imshow('sobel_y', sobel_y)
cv.imshow('edge strength', edge_strength)

cv.waitKey()
cv.destroyAllWindows()

