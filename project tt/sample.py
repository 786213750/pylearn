import random
import string
from PIL import Image
from claptcha import Claptcha
import cv2
import os
import sys

# Global variables

CharInCaptcha = 6
contours2 = []
num_array = []
path = 'C:\\Users\\Andrew\\Documents\\GitHub\\pylearn\\project tt\\images'

#Functions

def randomString():
    rndLetters = (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(CharInCaptcha))
    return "".join(rndLetters)

def exit():
    print("exit program based on string error")
    os.remove(os.path.join(path,StringName))
    sys.exit()

def tryImWrite(String,img,i):
    if (not os.path.isfile(os.path.join(path,String+"."+i+'.png'))):
        cv2.imwrite(os.path.join(path,String+"."+i+'.png'),img)
    else:
        tryImWrite(String,img,str(int(i)+1))
        
#Main

#Create Captcha and write to Images Folder
for i in range(1):
    String = randomString() 
    StringName = (String + '.png')
    c = Claptcha(String, "FreeMono.ttf",noise = 0.0)
    text, _ = c.write(os.path.join(path,StringName))

#Create Threshold Image, process contours, create ReturnImage
thresh,img = cv2.threshold(cv2.imread(os.path.join(path,StringName),cv2.IMREAD_GRAYSCALE),250,300,cv2.THRESH_BINARY)

im2,contours,hierarchy = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

returnImage = cv2.imread(os.path.join(path,StringName))

#save proper contours into contours2
#(eliminate contours within contours problem)
for i in range(len(contours)):
    if(hierarchy[0,i,3] != -1):
       (x,y,w,h) = cv2.boundingRect(contours[i])
       if (w*h > 100 and w < 100):
           #cv2.rectangle(a, (x,y), (x+w,y+h), (255,100,100), 1)
           contours2.insert(i,contours[i])

#Exception checker
if ( CharInCaptcha < len(contours2)):
    exit()

for i in range(len(contours2)):
    (_,_,w,_) = cv2.boundingRect(contours2[i])
    if (w > 40):
        exit()

#Create subImages for each character and write to seperate files.
#For repeated characters,first character represents character shown
#Second character and after represents the number of the same character

for i in range(len(contours2)):
    (x,y,w,h) = cv2.boundingRect(contours2[i])
    num_array.insert(i,x)
    
num_array.sort()

for i in range(len(contours2)):
    for j in range(len(contours2)):
        (x_val,_,_,_) = cv2.boundingRect(contours2[j])
        if (num_array[i] == x_val):
            (x,y,w,h) = cv2.boundingRect(contours2[j])
            cropped_RI = returnImage[y:y+h,x:x+w]
            tryImWrite(String[i],cropped_RI,'0')
            
os.remove(os.path.join(path,StringName))

#Temporary code

#cv2.imwrite(os.path.join(path,StringName),a)

#cv2.drawContours(img,contours,-1,(155,155,255),1)
#cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
#cv2.imshow('Display',a)
#cv2.waitKey()


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
