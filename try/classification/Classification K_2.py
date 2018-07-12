import numpy as np
import pandas as pd
import math
import warnings
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

style.use('fivethirtyeight')

dataset={'k': [[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
new_features =[5,7]


def k_nearest_neighbors(data,predict, k=3):
    if len(data)>= k:
        warnings.warn('k is cannot include all class!')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance =np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance,group])
    votes = [i[1] for i in sorted(distances)[:k]]
    #print(votes)
    #print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    
    return vote_result

result = k_nearest_neighbors(dataset,new_features,k=3)
print(result)
    


#for i in dataset:
    #for ii in dataset[i]:
        #plt.scatter(ii[0],ii[1],s=100, color=1)
        
        
        
[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0],new_features[1], color=result,s=100)
plt.show()



