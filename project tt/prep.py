import cv2
import tensorflow as tf
from random import shuffle
import pandas as pd
import numpy as np
import os
##import image path for nn
import sys

pathname = os.path.dirname(sys.argv[0])
Train_path = pathname + "\\image_train"
Test_path = pathname + "\\image_test"

IMG_size= 50
## set up for dict
s = pd.Series(list("abcdefghijklmnopqrstuvwxyz0123456789"+"abcdefghijklmnopqrstuvwxyz".upper()))
##create base one hot array
Bdict= pd.get_dummies(s)  
#print(Bdict)
Idict={}
## create one hot label dict
for i in range(len(s)):
    Idict[s[i]]=np.array(Bdict.ix[i,:])
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

def create_test_data():
    test_data=[]
    for img in os.listdir(Test_path):
        word_label= img.split('.')[0]
        path = os.path.join(Test_path,img)
        img =cv2.resize(cv2.imread(path),(IMG_size,IMG_size))
        test_data.append([np.array(img),np.array(label)])
    shuffle(test_data)
    np.save('test_data.npy',test_data)
    return(test_data)
create_test_data()

batch_size = 128
n_classes = 62
x = tf.placeholder('float', [None, 250])
y = tf.placeholder(tf.float32, [None, n_classes])



def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def maxpool2d(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def convolutional_neural_network(x):#, keep_rate):
    weights = {
        'W_conv1': tf.Variable(tf.random_normal([5, 5, 1, 32])),
        'W_conv2': tf.Variable(tf.random_normal([5, 5, 32, 64])),
        'W_fc': tf.Variable(tf.random_normal([12*12*64, 1024])),
        'out': tf.Variable(tf.random_normal([1024, n_classes]))
    }

    biases = {
        'b_conv1': tf.Variable(tf.random_normal([32])),
        'b_conv2': tf.Variable(tf.random_normal([64])),
        'b_fc': tf.Variable(tf.random_normal([1024])),
        'out': tf.Variable(tf.random_normal([n_classes]))
    }

    x = tf.reshape(x, shape=[-1, 48, 48, 1])
    conv1 = tf.nn.relu(conv2d(x, weights['W_conv1']) + biases['b_conv1'])
    conv1 = maxpool2d(conv1)
    conv2 = tf.nn.relu(conv2d(conv1, weights['W_conv2']) + biases['b_conv2'])
    conv2 = maxpool2d(conv2)

    fc = tf.reshape(conv2, [-1, 12*12*64])
    fc = tf.nn.relu(tf.matmul(fc, weights['W_fc']) + biases['b_fc'])

    output = tf.matmul(fc, weights['out']) + biases['out']
    return output


def train_neural_network(x):
    prediction = convolutional_neural_network(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits = prediction,lable = y) )
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    
    hm_epochs = 10
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())

        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(os.list.dir(Train_path)/batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
                epoch_loss += c

            print('Epoch', epoch, 'completed out of',hm_epochs,'loss:',epoch_loss)

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))

        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy:',accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))

#Testing Commit
train_neural_network(x)
