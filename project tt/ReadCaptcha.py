import os
import sys
import cv2
import CaptchaFunctions

#global variables

CharInCaptcha = 5
String = '12345'
StringName = 'input.png'
contours2 = []
num_array = []
listofletters = []
pathname = os.path.dirname(sys.argv[0])
path = pathname + "\\images"

#main

contours,hierarchy,returnImage = CaptchaFunctions.ImageCreate(StringName,path)
CaptchaFunctions.elimContours(contours,contours2,hierarchy)
    
#Exception checker
if (CharInCaptcha < len(contours2)):
    print('read failed')
    exit


for i in range(len(contours2)):
    (_,_,w,_) = cv2.boundingRect(contours2[i])
    if (w > 40):
        print('read failed')
        exit

listofletters = CaptchaFunctions.cropContours(contours2,num_array,String,returnImage,path)

CaptchaFunctions.writeImages(listofletters,String,path)
