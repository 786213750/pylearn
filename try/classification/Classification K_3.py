import numpy as np
import pandas as pd
import math
import warnings
import random
from collections import Counter

accuracies=[]
for i in range(5):
    def k_nearest_neighbors(data,predict, k=3):
        if len(data)>= k:
            warnings.warn('k is cannot include all class!')
        distances = []
        for group in data:
            for features in data[group]:
                euclidean_distance =np.linalg.norm(np.array(features)-np.array(predict))
                distances.append([euclidean_distance,group])
        
        votes = [i[1] for i in sorted(distances)[:k]]
        vote_result = Counter(votes).most_common(1)[0][0]
        confidence = Counter(votes).most_common(1)[0][1]/k
        
        return vote_result,confidence
    
    df = pd.read_csv('breast-cancer-wisconsin.data.txt')
    df.replace('?',-99999,inplace=True)
    df.drop(['id'],1,inplace=True)
    full_data =df.astype(float).values.tolist()
    #print(full_data[:5])
    random.shuffle(full_data)
    
    test_size=0.4
    train_set ={2:[],4:[]}
    test_set = {2:[],4:[]}
    train_data = full_data[:int(test_size*len(full_data))]
    test_data = full_data[int(test_size*len(full_data)):]
    
    
    for i in train_data:
        train_set[i[-1]].append(i[:-1])
    
    for i in test_data:
        test_set[i[-1]].append(i[:-1])
    
    #print(train_set)    
    correct = 0
    total = 0
    
    for group in test_set:
        for data in test_set[group]:
            #print(data)
            vote,confidence =k_nearest_neighbors(train_set,data,k=5)
            if group == vote:
                correct+=1
    
            total+=1
    
    #print('Accuracy',correct/total)
    accuracies.append(correct/total)
print(sum(accuracies)/len(accuracies))
    
