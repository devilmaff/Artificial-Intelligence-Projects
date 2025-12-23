import urllib.request
import cv2
import numpy as np
import imutils


url='http://your_ip_address/shot.jpg'

while True:
    imgPath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()), dtype=np.uint8)
    frame=cv2.imdecode(imgNp, -1)

    frame=imutils.resize(frame,width=450)
    cv2.imshow("Frame",frame)
    if ord('q')==cv2.waitKey(1):
        exit(0)
