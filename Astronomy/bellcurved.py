#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:13:43 2020

@author: omnizon
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from scipy.optimize import curve_fit

style.use('ggplot')
y = np.loadtxt('/home/omnizon/Desktop/Astronomy/148_2019-11-15_03_07_42_UTC.csv')
x = np.linspace(-1000, 995, num = 400)

def maskR(x,y):
    ymax=np.amax(y)
    xmax=x[y==ymax]
    y21= y[x<xmax-250] 
    x21= x[x<xmax-250]
    y22= y[x>xmax+250] 
    x22= x[x>xmax+250]
    x2=np.concatenate((x21,x22),axis=0)
    y2=np.concatenate((y21,y22),axis=0)
    
    
    return x2,y2
def func(x,a,b,c,d,e,f):
    z= a*np.exp(-0.5*(((x-c)*0.5/b)**2))+ d*np.exp(-0.5*(((x-e)*0.5/f)**2))
    return z
    
x2,y2=maskR(x,y)
coef= np.polyfit(x2, y2, 2)
poly = np.poly1d(coef)
new_x2= np.linspace(x[0],x[-1])
new_y2=poly(new_x2)

#plt.plot(x,y, label="Unmasked")
#plt.plot(new_x2,new_y2, label="Masked")
plt.title('Data')
plt.ylabel('Voltage')
plt.xlabel('Frequency')

y3= poly(x)
y3= np.subtract(y,y3)
plt.plot(x,y3)
init_guess=[1, np.std(y3), np.mean(y3),1,1,1]
popt, pcov = curve_fit(func, x, y3, init_guess)

plt.plot(x, func(x, *popt))
