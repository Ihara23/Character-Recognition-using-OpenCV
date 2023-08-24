import numpy as np
import cv2

BGR_im = cv2.imread("im1.jpg",1)
im = cv2.imread("im1.jpg",0)
thresh,im = cv2.threshold(im,127,255,cv2.THRESH_BINARY_INV)
im2 = im.copy()

contours, hi =cv2.findContours(im,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
i=0
for con in contours:
    x,y,w,h = cv2.boundingRect(con)
    cv2.rectangle(BGR_im,(x,y), (x+w,y+h),(0,255,0),1)
    cv2.imshow("data", BGR_im)
    letter = im[y:y+h,x:x+w]
    letter = cv2.resize(letter,[15,20])
    f_name = "dbase/l"+ str(26-i) + ".jpg"
    cv2.imwrite(f_name,letter)
    i=i+1
    cv2.waitKey(500)
cv2.destroyAllWindows()