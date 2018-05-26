import pandas as pd
import numpy as np

df= pd.DataFrame([[1,6,6],[1,5,2],[887,67,4]],index=['a','b','c'],columns=['d', 'e','f'])
df.to_pickle('testdata.pickle')
print(df)