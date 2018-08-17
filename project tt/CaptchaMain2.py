import CaptchaFunctions
import os
import sys
import cv2
import Createxml
from claptcha import Claptcha

# Global variables

CharInCaptcha = 5
pathname = os.path.dirname(__file__)
path = pathname + "/images"

#Main

for _ in range(1):
    #Create Captcha and write to Images Folder
    contours2 = []
    num_array = []
    String = CaptchaFunctions.randomString(CharInCaptcha)
    c = Claptcha(String, "FreeMono.ttf",noise = 0.0)
    String = CaptchaFunctions.getavailname(path,String)
    StringName = (String + '.png')
    text, _ = c.write(os.path.join(path,StringName))
    print(path)
    

    
    contours,hierarchy,returnImage = CaptchaFunctions.ImageCreate(StringName,path)
    CaptchaFunctions.elimContours(contours,contours2,hierarchy)
    
    #Exception checker
##    if (CharInCaptcha < len(contours2)):
##        os.remove(os.path.join(path,StringName))
##        
##        continue
    try:
        for i in range(len(contours2)):
            (_,_,w,_) = cv2.boundingRect(contours2[i])
            if (w > 40):
                os.remove(os.path.join(path,StringName))
                print('lol')
                raise CaptchaFunctions.Continue1
    except CaptchaFunctions.Continue1:
        print(String)
        continue
        
    
    coords = CaptchaFunctions.returncoords(contours2,num_array,String,returnImage,path)
    for i in range(len(coords)):
        tl = (coords[i][0],coords[i][1])
        br = (coords[i][0]+coords[i][2],coords[i][1]+coords[i][3])
        
        Createxml.write_xml(path,os.path.join(path,String + '.png'),String + '.' + str(i) + '.png',[String],[tl],[br],CaptchaFunctions.trypath(os.path.dirname(path) + "//xml"))
        
         
