import random
import string
from PIL import Image
from claptcha import Claptcha
import cv2


def randomString():
    rndLetters = (random.choice(string.ascii_uppercase) for _ in range(6))
    return "".join(rndLetters)
for i in range(2):
    c = Claptcha(randomString, "FreeMono.ttf",noise = 0.0)
    text, _ = c.write('t' + str(i) + '.png')

thresh,img = cv2.threshold(cv2.imread("t0.png",cv2.IMREAD_GRAYSCALE),200,300,cv2.THRESH_BINARY)
cv2.imwrite("b.png",img)

im2,contours,hierarchy = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
cv2.imwrite("c.png",im2)

for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)
    cv2.rectangle(img, (x,y), (x+w,y+h), (100,255,100), 1)
    

#cv2.drawContours(img,contours,-1,(155,155,255),1)
cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
cv2.imshow('Display',img)
cv2.waitKey()
