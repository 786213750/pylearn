import random
import string
from PIL import Image
from claptcha import Claptcha
import cv2
import os
import sys
import Createxml

#class

class Continue1(Exception):
    pass

#Functions

def randomString(CharInCaptcha):
    rndLetters = (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(CharInCaptcha))
    return "".join(rndLetters)

def tryImWrite(String,img,path):
    i='0'
    while (os.path.isfile(os.path.join(path,String+'.'+i+'.png'))):
        i = str(int(i)+1)
    else:
        cv2.imwrite(os.path.join(path,String+"."+i+'.png'),img)
        return os.path.join(path,String+"."+i+'.png'),String+"."+i+'.png'
     

#Create Threshold Image, process contours, create ReturnImage
def ImageCreate(StringName,path):
    
    thresh,img = cv2.threshold(cv2.imread(os.path.join(path,StringName),cv2.IMREAD_GRAYSCALE),250,300,cv2.THRESH_BINARY)
    
    im2,contours,hierarchy = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

    returnImage = cv2.imread(os.path.join(path,StringName))
    return contours,hierarchy,returnImage

#save proper contours into contours2
#(eliminate contours within contours problem)
def elimContours(contours,contours2,hierarchy):
    for i in range(len(contours)):
        if(hierarchy[0,i,3] != -1):
           (x,y,w,h) = cv2.boundingRect(contours[i])
           if (w*h > 100 and w < 100):
               #cv2.rectangle(a, (x,y), (x+w,y+h), (255,100,100), 1)
               contours2.insert(i,contours[i])

#Create subImages for each character and write to seperate files.
#For repeated characters,first character represents character shown
#Second character and after represents the number of the same character
def cropContours(contours2,num_array,String,returnImage,path):
    for i in range(len(contours2)):
        (x,y,w,h) = cv2.boundingRect(contours2[i])
        num_array.insert(i,x)
    returnlist = []    
    num_array.sort()
    for i in range(len(contours2)):
        for j in range(len(contours2)):
            (x_val,_,_,_) = cv2.boundingRect(contours2[j])
            if (num_array[i] == x_val):
                (x,y,w,h) = cv2.boundingRect(contours2[j])
                cropped_RI = returnImage[y:y+h,x:x+w]
                returnlist.append(cropped_RI)
    return returnlist

def returncoords(contours2,num_array,String,returnImage,path):
    for i in range(len(contours2)):
        (x,y,w,h) = cv2.boundingRect(contours2[i])
        num_array.insert(i,x)
    returnlist = []    
    num_array.sort()
    for i in range(len(contours2)):
        for j in range(len(contours2)):
            (x_val,_,_,_) = cv2.boundingRect(contours2[j])
            if (num_array[i] == x_val):
                (x,y,w,h) = cv2.boundingRect(contours2[j])
                dimensions = [x,y,w,h]                
                returnlist.append(dimensions)
    return returnlist

def writeImages(listofImages,String,path):
    for i in range(len(listofImages)):
        s,name = tryImWrite(String[i],listofImages[i],path)
        Createxml.write_xml(path,s,name,[String[i]],[(0,0)],[(10,10)],trypath(os.path.dirname(path) + "\\xml"))

def trypath(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path    
       
def getavailname(path,string):
    i = 0
    while (os.path.isfile(os.path.join(path,string + '.' + str(i)))):
        i += 1
    return string + '.' + str(i)

#Temporary code

##def writeImages2(listofImages,String,path):
##    for i in range(len(listofImages)):
##        if String[i].isupper():
##            s = String[i] + "_up"
##            tryImWrite(String[i],listofImages[i],trypath(path + "\\" + s))
##        else:
##            tryImWrite(String[i],listofImages[i],trypath(path + "\\" + String[i]))
##

#cv2.drawContours(returnImage,contours,-1,(155,155,255),1)
#cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
#cv2.imshow('Display',returnImage)
#cv2.waitKey()


