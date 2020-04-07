#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:00:51 2020

@author: omnizon
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')
y = np.loadtxt('/home/omnizon/Desktop/Astronomy/Test_2019-11-15_02_49_23_UTC.csv')
x = np.linspace(-1000, 995, num = 400)

def maskR(x,y):
    ymax=np.amax(y)
    xmax=x[y==ymax]
    y21= y[x<xmax-125] 
    x21= x[x<xmax-125]
    y22= y[x>xmax+125] 
    x22= x[x>xmax+125]
    x2=np.concatenate((x21,x22),axis=0)
    y2=np.concatenate((y21,y22),axis=0)
    
    
    return x2,y2


x2,y2=maskR(x,y)
coef= np.polyfit(x2, y2, 3)
poly = np.poly1d(coef)
new_x2= np.linspace(x[0],x[-1])
new_y2=poly(new_x2)

plt.plot(x,y, label="Unmasked")
plt.plot(new_x2,new_y2, label="Masked")
plt.title('Data')
plt.ylabel('Voltage')
plt.xlabel('Frequency')

y3= poly(x)
y3= np.subtract(y,y3)
plt.plot(x,y3)