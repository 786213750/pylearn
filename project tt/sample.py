import random
import string
from PIL import Image
from claptcha import Claptcha
import cv2
import os

def randomString():
    rndLetters = (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    return "".join(rndLetters)

for i in range(1):
    z = randomString()
    f = (z + '.png')
    c = Claptcha(z, "FreeMono.ttf",noise = 0.0)
    text, _ = c.write(f)

thresh,img = cv2.threshold(cv2.imread(f,cv2.IMREAD_GRAYSCALE),250,300,cv2.THRESH_BINARY)

im2,contours,hierarchy = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

a = cv2.imread(f)

for i in range(len(contours)):
    if(hierarchy[0,i,3] != -1):
       (x,y,w,h) = cv2.boundingRect(contours[i])
       cv2.rectangle(a, (x,y), (x+w,y+h), (255,100,100), 1)
    
cv2.imwrite(f,a)
#cv2.drawContours(img,contours,-1,(155,155,255),1)
#cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
#cv2.imshow('Display',a)
#cv2.waitKey()
