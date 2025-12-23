import cv2

import imutils

img = cv2.imread('1.jpg')

resizedImg = imutils.resize(img, width=50)

cv2.imwrite('resizedImage2.jpg', resizedImg)
