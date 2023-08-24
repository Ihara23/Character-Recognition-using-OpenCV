import numpy as np
import cv2
import os
import math


d_im = np.zeros([20,15], dtype= 'uint8') #database images 20=rows 
for f in range(1,27,1):
    ff="dbase/l" + str(f) + ".jpg"
    d_l=cv2.imread(ff,0)
    thresh,d_l = cv2.threshold(d_l,127,255,cv2.THRESH_BINARY)
    d_im = np.append(d_im,d_l, axis = 1)

def mean2(x):
    y=np.sum(x)/np.size(x)
    return y

def corr2(a,b):
    a=a-mean2(a)
    b=b-mean2(b)
    r=(a*b).sum()/math.sqrt((a*a).sum()*(b*b).sum())
    return r


BGR_im = cv2.imread("im2.jpg",1)
im = cv2.imread("im2.jpg",0)
thresh,BW_im = cv2.threshold(im,150,255,cv2.THRESH_BINARY_INV)
im2 = BW_im.copy()

letter_array = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
contours, hi =cv2.findContours(BW_im,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
i=0
corr2_val=np.zeros(26)
for con in contours:
    x,y,w,h = cv2.boundingRect(con)
    cv2.rectangle(BGR_im,(x,y), (x+w,y+h),(0,255,0),1)
    cv2.imshow("unknown", BGR_im)
    letter = BW_im[y:y+h,x:x+w]
    letter = cv2.resize(letter,[15,20]) # width=columns, height=rows  
    i=i+1
    for j in range(0,26):
        d_l = d_im[0:20,15+15*j:30+15*j]
        corr2_val[j]=corr2(d_l,letter)
    j_ind = np.where(corr2_val==max(corr2_val))
    #print(str(j_ind[0][0]+1))
    print(letter_array[j_ind[0][0]])
    cv2.waitKey(500)
    if(cv2.waitKey(1) & 0xFF ==ord('q')):
        cv2.destroyAllWindows()
        break
