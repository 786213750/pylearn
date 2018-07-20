import cv2
import tensorflow as tf
from random import shuffle
import pandas as pd
import numpy as np
import os
import tflearn
import sys
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
##import image path for nn
pathname = os.path.dirname(sys.argv[0])
Train_path = pathname + "\\images_train"
Test_path = pathname +"\\images_test"

IMG_size= 50
LR = 1e-3

MODEL_NAME = 'Captcha-{}-{}.model'.format(LR, '2conv-basic')



## set up for dict
base_s =list("0123456789"+"abcdefghijklmnopqrstuvwxyz".upper()+"abcdefghijklmnopqrstuvwxyz")
s = pd.Series(base_s)

##create base one hot array
Bdict= pd.get_dummies(s)  
#print(Bdict)
Idict={}
## create one hot label dict
for i in range(len(s)):
    Idict[s[i]]=np.array(Bdict.ix[i,:])
#print(len(Idict))
## create the training dataset



def create_train_data():
    training_data=[]
    for img in os.listdir(Train_path):
        word_label= img.split('.')[0]
        label= Idict[word_label]
        path = os.path.join(Train_path,img)
        img =cv2.resize(cv2.imread(path,cv2.IMREAD_GRAYSCALE),(IMG_size,IMG_size))
        training_data.append([np.array(img),np.array(label)])
    shuffle(training_data)
    np.save('train_data.npy',training_data)
    return(training_data)
train = create_train_data()

def create_test_data():
    test_data=[]
    for img in os.listdir(Test_path):
        word_label= img.split('.')[0]
        path = os.path.join(Test_path,img)
        label= Idict[word_label]
        img =cv2.resize(cv2.imread(path,cv2.IMREAD_GRAYSCALE),(IMG_size,IMG_size))
        test_data.append([np.array(img),np.array(label)])
    shuffle(test_data)
    np.save('test_data.npy',test_data)
    return(test_data)
test = create_test_data()


convnet = input_data(shape=[None, IMG_size, IMG_size, 1], name='input')

convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 128, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)

convnet = fully_connected(convnet, 62, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet, tensorboard_dir='log')

if os.path.exists('{}.meta'.format(MODEL_NAME)):
    model.load(MODEL_NAME)
    print('model loaded!')


X = np.array([i[0] for i in train]).reshape(-1,IMG_size,IMG_size,1)
Y = [i[1] for i in train]


test_x = np.array([i[0] for i in test]).reshape(-1,IMG_size,IMG_size,1)
test_y = [i[1] for i in test]
def train_model(X,Y,test_x,test_y):
    model.fit({'input': X}, {'targets': Y}, n_epoch=10, validation_set=({'input': test_x}, {'targets': test_y}), 
              snapshot_step=500, show_metric=True, run_id=MODEL_NAME)
    model.save(MODEL_NAME)

def predict_model(X):
    word=[]
    Y=(model.predict(X))
    for i in Y:
        word.append(base_s[np.where(i==max(i))[0][0]])
    return "".join(word)
Train=[]
for img in os.listdir(Train_path):
    path = os.path.join(Train_path,img)
    img =cv2.resize(cv2.imread(path,cv2.IMREAD_GRAYSCALE),(IMG_size,IMG_size))
    Train.append(img)
X = np.array([i[0] for i in train]).reshape(-1,IMG_size,IMG_size,1)    
print(predict_model(X))
