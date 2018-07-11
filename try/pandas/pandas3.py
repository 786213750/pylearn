import pandas as pd
import numpy as np

df1=pd.read_pickle('testdata.pickle')
df2=pd.read_pickle('testdata.pickle')
df3=pd.read_pickle('testdata.pickle')
df4= pd.DataFrame(np.ones((3,3))*3,index=['b','c','d'],columns=['e','f','g'])
print(df1)
res=pd.concat([df1,df4],axis=1,join_axes=[df1.index])
print(res)
res1=pd.concat([df1,df4],axis=1,join_axes=[df4.index])
print(res1)
res2=pd.concat([df1,df4],axis=1,join='inner')
print(res2)
res3=df1.append([df2,df4],ignore_index=True)
print(res3)
s1=pd.Series([1,2,3],index=['d','e','f'])
res4=df1.append(s1,ignore_index=True)
print(res4)