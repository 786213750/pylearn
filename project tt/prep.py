import cv2
import tensorflow as tf
from random import shuffle
import pandas as pd
import numpy as np
import os
<<<<<<< HEAD

Train_path="C:\\Users:\\Admin\\Downloads\\PortableGit\\ProjectTT\\pylearn\\project tt\\images"
IMG_size= 50
s = pd.Series(list("abcdefghijklmnopqrstuvwxyz0123456789"))
#print(s)
=======
##import image path for nn
Train_path="c:\\thomas\\project tt\\t1"
IMG_size= 50
## set up for dict
s = pd.Series(list("abcdefghijklmnopqrstuvwxyz0123456789"+"abcdefghijklmnopqrstuvwxyz".upper()))
##create base one hot array
>>>>>>> origin/master
Bdict= pd.get_dummies(s)  

#print(Bdict)
Idict={}
## create one hot label dict
for i in range(len(s)):
    Idict[s[i]]=np.array(Bdict.ix[i,:])
    
#print(Idict)
#print(Idict)
## create the training dataset
def create_train_data():
    training_data=[]
    for img in os.listdir(Train_path):
        word_label= img.split('.')[0]
        label= Idict[word_label]
        path = os.path.join(Train_path,img)
        img =cv2.resize(cv2.imread(path),(IMG_size,IMG_size))
        training_data.append([np.array(img),np.array(label)])
    shuffle(training_data)
    np.save('train_data.npy',training_data)
    return(training_data)
create_train_data()


    
