import CaptchaFunctions
import os
import sys
import cv2
from claptcha import Claptcha

# Global variables

CharInCaptcha = 5
pathname = "C:\\object-detection-darkflow-master"
path = pathname + "\\images"

#Main

for _ in range(1000):
    #Create Captcha and write to Images Folder
    contours2 = []
    num_array = []
    String = CaptchaFunctions.randomString(CharInCaptcha) 
    StringName = (String + '.png')
    c = Claptcha(String, "FreeMono.ttf",noise = 0.0)
    text, _ = c.write(os.path.join(path,StringName))
    
    contours,hierarchy,returnImage = CaptchaFunctions.ImageCreate(StringName,path)
    CaptchaFunctions.elimContours(contours,contours2,hierarchy)
    
    #Exception checker
    if (CharInCaptcha < len(contours2)):
        os.remove(os.path.join(path,StringName))
        continue

    try:
        for i in range(len(contours2)):
            (_,_,w,_) = cv2.boundingRect(contours2[i])
            if (w > 40):
                os.remove(os.path.join(path,StringName))
                print('lol')
                raise CaptchaFunctions.Continue1
    except CaptchaFunctions.Continue1:
        continue

    #CaptchaFunctions.writeImages(CaptchaFunctions.cropContours(contours2,num_array,String,returnImage,path),String,path)
    CaptchaFunctions.writeImages2(CaptchaFunctions.cropContours(contours2,num_array,String,returnImage,path),String,path)
    os.remove(os.path.join(path,StringName))
    
