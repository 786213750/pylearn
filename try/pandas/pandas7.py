import pandas as pd
import numpy as np

df1=pd.read_pickle('testdata.pickle')
df4= pd.DataFrame(np.ones((3,3))*3,index=['b','c','d'],columns=['e','f','g'])
df1.ix[1,1]=np.nan
df1.fillna(-99999,inplace=True)
print(df1)
df1['label']=df1['d'].shift(-2)
print(df1)