import pandas as pd
import numpy as np

df1=pd.read_pickle('testdata.pickle')
df2=pd.read_pickle('testdata.pickle')
df3=pd.read_pickle('testdata.pickle')
df4= pd.DataFrame(np.ones((3,3))*3,
                  index=['b','c','d'],
                  columns=['e','f','g'])
print(df4)
#res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)#use pickle is much better
#print(res)
res1=pd.concat([df1,df4],join='inner',ignore_index=False)
res2=pd.concat([df1,df4],join='inner',ignore_index=True)
print(res1)
print(res2)
