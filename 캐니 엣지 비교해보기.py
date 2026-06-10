#5.14 케니 에지 실험
import cv2 as cv

img=cv.imread('soccer.jpg')

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny1=cv.Canny(gray, 50, 150) #1:3
canny2=cv.Canny(gray, 50, 200) #1:4
canny3=cv.Canny(gray, 150, 50) #3:1
canny4=cv.Canny(img, 50, 150)

cv.imshow('Original', gray)
cv.imshow('canny1', canny1)
cv.imshow('canny2', canny2)
cv.imshow('canny3', canny3)
cv.imshow('canny4', canny4)

cv.waitKey()
cv.destroyAllWindows()