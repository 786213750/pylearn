import cv2
import tensorflow as tf
from random import shuffle
import pandas as pd
import numpy as np
import os

Train_path="C:\Andrew\Documents\GitHub\pylearn\project tt"
IMG_size= 50
s = pd.Series(list("abcdefghijklmnopqrstuvwxyz0123456789"))
Bdict= pd.get_dummies(s)  
#print(Bdict)
Idict={}
for i in range(len(s)):
    Idict[s[i]]=np.array(Bdict.ix[i,:])
#print(Idict)
#
def create_train_data():
    training_data=[]
    for img in os.listdir(Train_path):
        word_label= img.splite('.')[0]
        label= Idict[word_label]
        path = os.path.join(Train_path,img)
        img =cv2.resize(cv2.imread(path),(IMG_size,IMG_size))
        training_data.append([np.array(img),np.array(label)])
    shuffle(training_data)
    np.save('train_data.npy',training_data)
    return(training_data)

    
