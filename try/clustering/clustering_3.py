import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import random
style.use('ggplot')


X=np.array([[1,2],
            [1.5,1.8],
            [5,8],
            [8,8],
            [1,0.6],
            [9,11]])


colors=['g','r','c','b','k','o']*10

class K_Means:
    def __init__(self,k=2,tol=0.001,max_iter=300):
        self.k=k
        self.tol=tol
        self.max_iter =max_iter
        
    def fit(self,data):
        self.centroids ={}
        for i in range(self.k):
            self.centroids[i]= data[i]
        
        for _ in range(self.max_iter):
            self.classifications ={}
            for i in range(self.k):
                self.classifications[i]=[]
            
            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
              
            prev_centroids = dict(self.centroids)
            
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification],axis=0)
                
           
            optimized =True
            
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100)>self.tol:
                    print(np.sum((current_centroid-original_centroid)/original_centroid*100))
                    optimized = False
                   
            if optimized:
                break
            
    def predict(self,data):
        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
    
clf= K_Means()
clf.fit(X)
    
for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0],clf.centroids[centroid][1],
                marker="o",c='k',s=30,linewidths=5)
    
for classification in clf.classifications:
    color = colors[classification]
    #print(color)
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0],featureset[1], marker='x',c=color,s=30)
        #print(featureset)

unknows = np.array([[1,8],[.1,-1],[1,0],[3,3],[4,7],[10,.8]])
for unknow in unknows:
    classification = clf.predict(unknow)
    plt.scatter(unknow[0],unknow[1],marker='*',c=colors[classification],s=30)
plt.show()
