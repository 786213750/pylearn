import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd
import pickle
accuracies=[]
for i in range(10):
    df= pd.read_csv('breast-cancer-wisconsin.data.txt')
    df.replace("?",-99999, inplace=True)
    df.drop(['id'],1,inplace=True)
    
    X=np.array(df.drop(['class'],1))
    y=np.array(df['class'])
    
    X_train,X_test,Y_train,Y_test=cross_validation.train_test_split(X,y,test_size=0.2)
    
    clf = neighbors.KNeighborsClassifier(n_jobs=-1)
    clf.fit(X_train,Y_train)
    #with open('classificationKN','wb') as f:
     #   pickle.dump(clf,f)
    #pickle_in= open('classificationKN','rb')
    #clf=pickle.load(pickle_in)
    accuracy =clf.score(X_test,Y_test)
    #print(accuracy)
    ex_1=np.array([[1,2,3,1,2,1,4,4,3],[7,6,5,9,1,9,4,4,1]])
    ex_2=np.array([4,1,3,1,2,1,4,4,3])
    #print(ex_2)
    #ex_2.reshape(1,-1)
    #print(ex_2)
    predict_value=clf.predict(ex_1)
    #print(predict_value,accuracy)
    accuracies.append(accuracy)

print(sum(accuracies)/len(accuracies))