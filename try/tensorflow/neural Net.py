import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist=input_data.read_data_sets("official/mnist/dataset.py", one_hot=True)

n_nodes_hl1 =500
n_nodes_hl2 =500
n_nodes_hl3 =500 #length of hidden layer

n_classes = 10 # #of classes
batch_size = 100 #100 picture each time

x = tf.placeholder('float',[None,784])
y = tf.placeholder('float')

def neural_nerwork_model(data):
    # (input_data*weights)+biases 
    
    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([784,n_nodes_hl1])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl1))}
    
    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1,n_nodes_hl2])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl2))}
    
    hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2,n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl3))}
    
    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3,n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal([n_classes]))}    
    
    l1= tf.add(tf.matmul(data,hidden_1_layer['weights']) + hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)
    
    l2= tf.add(tf.matmul(l1,hidden_2_layer['weights']) + hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)
    
    l3= tf.add(tf.matmul(l2,hidden_3_layer['weights']) + hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)    
    
    output = tf.matmul(l3,output_layer['weights']) + output_layer['biases']
    
    return output

def train_neural_network(x):
    prediction = nre