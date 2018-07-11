import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
import math

xs=np.array(np.arange(6)+1,dtype=np.float64)
ys=np.array([5,4,6,5,6,7],dtype=np.float64)
mean_x = mean(xs)
mean_y = mean(ys)

def squared_error(y_o,y_l):
    return sum((y_l-y_o)**2)
def coefficient_of_determination(y_o,y_l):
    y_mean_line = [mean(y_o) for y in y_o]
    y_mean_error = squared_error(y_o,y_mean_line)
    y_line_error = squared_error(y_o,y_l)
    return 1-y_line_error/y_mean_error

def best_fit_sni(xs,ys):
    m= (mean_x*mean_y-mean(xs*ys))/(mean_x**2-mean(xs**2))
    b=mean_y-mean_x*m
    return m,b

m,b= best_fit_sni(xs,ys)

#print(m,b)
line=[m*x+b for x in xs]
r=coefficient_of_determination(ys,line)
print(r)
predict_x= np.array([8,9,12])
predict_y= m*predict_x+b

plt.plot(predict_x,predict_y)
plt.scatter(xs,ys)
plt.plot(xs,line)
plt.show()