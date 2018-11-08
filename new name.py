import cv2
import numpy as np

img = cv2.imread('rotateInitial.png',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),12.7,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

angle = 45
width = int((np.cos(np.deg2rad(angle))*640)+(np.cos(np.deg2rad(90-angle))*480))
height = int((np.sin(np.deg2rad(angle))*640)+(np.sin(np.deg2rad(90-angle))*480))

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
res = cv2.resizeWindow( dst, (width,height))


cv2.imshow('image', res)
