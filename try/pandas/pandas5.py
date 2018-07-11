import numpy as np
import pandas as pd

left= pd.DataFrame({'key1':['K0','K0','K1','K2'],
                    'key2':['K0','K1','K0','K1'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3']})
right= pd.DataFrame({'key1':['K0','K1','K1','K2'],
                     'key2':['K0','K0','K0','K0'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']})
res=pd.merge(left,right,on=['key1','key2'])
print(res)
