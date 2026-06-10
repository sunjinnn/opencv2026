import cv2 as cv
#영상도 회색이미지로 바꿔가면서 확인해보기

img=cv.imread('rose.jpg')
patch=img[150:200, 170:270, :]

img=cv.rectangle(img, (170,250), (150,200), (255,0,0), 3)
patch1=cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
patch2=cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
patch3=cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)


cv.imshow('Original', img)
cv.imshow('Resize nearest', patch1)
cv.imshow('Resize bilinear', patch2)
cv.imshow('Resize bicubic', patch3)

cv.waitKey()
cv.destroyAllWindows()

