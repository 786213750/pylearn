import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data= pd.Series ( np.random.randn(1000),index=np.arange(1000))
#data=data.cumsum()
#data.plot()
#plt.show()

data= pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))

data=data.cumsum()
data['E']=np.arange(1000)
#print(data.head(10))
ax=data.plot.scatter(x='E',y='A',color='Blue', label='Class1')
ax1=data.plot.scatter(x='A',y='C',color='Green', label='Class2')
data.plot.scatter(x='A',y='B',color='DarkBlue', label='Class3',ax=ax1)
plt.show()
