import urllib.request
import cv2
import numpy as np
import time
URL = "http://your_ip_address/shot.jpg"


alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)



while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr ,-1)
   
    
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,0),5)
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(20)
    if key == 27:
        break

cv2.destroyAllWindows()
