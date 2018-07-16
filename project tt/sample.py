import random
import string
from PIL import Image
from claptcha import Claptcha
import cv2
import os

def CombineBounds(y1,y2,w1,w2):
    return 
    

def randomString():
    rndLetters = (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    return "".join(rndLetters)

path = 'C:\\Users\\Andrew\\Documents\\GitHub\\pylearn\\project tt\\images'
for i in range(1):
    z = randomString()
    f = (z + '.png')
    c = Claptcha(z, "FreeMono.ttf",noise = 0.0)
    text, _ = c.write(os.path.join(path,f))

thresh,img = cv2.threshold(cv2.imread(os.path.join(path,f),cv2.IMREAD_GRAYSCALE),250,300,cv2.THRESH_BINARY)

im2,contours,hierarchy = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

a = cv2.imread(os.path.join(path,f))

##for i in range(len(contours)):
##    if(hierarchy[0,i,3] != -1):
##        for j in range(len(contours) -1):
##            (x1,y1,w1,h1) = cv2.boundingRect(contours[i])
##            (x2,y2,w2,h2) = cv2.boundingRect(contours[j])
##            if (x1 > x2 and w1 < w2):
##                Y1,Y2 = y1,y1+h1
##                if (y2 < y1):
##                    Y1 = y2
##                if (y2+h2 > y1+h1):
##                    Y2 = y2+h2
##                #cv2.rectangle(a, (x2,Y1), (x2+w2,Y2), (255,100,100), 1)
##            #else:
##                #cv2.rectangle(a, (x1,y1), (x1+w1,y1+h1), (255,100,100), 1)

contours2 = []
for i in range(len(contours)):
    if(hierarchy[0,i,3] != -1):
       (x,y,w,h) = cv2.boundingRect(contours[i])
       print(x,y,w,h)
       if (w*h > 100):
           cv2.rectangle(a, (x,y), (x+w,y+h), (255,100,100), 1)
           contours2.insert(i,contours[i])
    
num_array = []

for i in range(len(contours2)):
    (x,y,w,h) = cv2.boundingRect(contours2[i])
    num_array.insert(i,x)
    
print(num_array)
num_array.sort()
print(num_array)

for i in range(len(contours2)):
    for j in range(len(contours2)):
        (x_val,_,_,_) = cv2.boundingRect(contours2[j])
        if (num_array[i] == x_val):
            (x,y,w,h) = cv2.boundingRect(contours2[j])
            crop_a = a[y:y+h,x:x+w]
            cv2.imwrite(os.path.join(path,z[i]+'.png'),crop_a)

cv2.imwrite(os.path.join(path,f),a)

#cv2.drawContours(img,contours,-1,(155,155,255),1)
#cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
#cv2.imshow('Display',a)
#cv2.waitKey()
