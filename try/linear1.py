import pandas as pd
import math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
#df= pd.DataFrame(np.random.randn(15,3),columns=['d', 'e','f'])
df1= pd.DataFrame([[1,1,1],[2,2,2],[3,3,4],[5,4,3],[9,8,8],[15,20,13],[25,23,24],[28,25,23],[30,33,30]],columns=['d', 'e','f'])
df2= pd.DataFrame(np.random.randn(5,3),columns=list('def'))
df=pd.concat([df1,df2],axis=0,ignore_index=True)
print(df)
X=np.array(df.drop('f',1))
Y=np.array(df['f'])
#print(X)
#print(Y)
X=preprocessing.scale(X)
#print(X)
#print(Y)

X_train,X_test,Y_train,Y_test=cross_validation.train_test_split(X, Y, test_size=0.2)
#print('xtrain',X_train)
#print('xtest',X_test)
#print('ytrain',Y_train)
#print('ytest',Y_test)

#clf=svm.SVR(kernel='poly')
clf=LinearRegression()
clf.fit(X_train,Y_train)
accuracy=clf.score(X_test,Y_test)
#print(accuracy)
s1=np.array([[31,21],[23,46],[19,50],[50,89],[3,95]])
forcast_set=clf.predict(s1)
print(forcast_set,accuracy)
df['Forecast']=np.nan
last_index= df1.iloc[-1].name
print(last_index)
#last_unix=last_date.timestamp()
#print(last_unix)
print(last_index)
for i in forcast_set:
    last_index+=1
    print(last_index)
    df.iloc[last_index]=[np.nan for _ in range(len(df.columns)-1)]+[i]

df['d'].plot()
df['Forecast'].plot()   
plt.show()