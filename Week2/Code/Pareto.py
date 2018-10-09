# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:27:07 2018

@author: Jamal Khan
"""

import pylab
import random
import math
import scipy
#from scipy import integrate

data = []
s1 = 0
s2 = 0
n = 40000


def st(vb):
    f = lambda x : (math.exp(-x/6))/6
    y = scipy.integrate.quad(f, 0, vb)
    t = y[0]
    return t

def rt(vb):
    t = (math.exp(-x/6))/6 
    return t

for i in range(n):
    x = 0
    u = random.uniform(0, 1.0)
    while True:
        x1 = x - ((st(x)-u))/(rt(x))
        x2 = x
        x = x1
        if abs(x2-x1)<0.000001:
            break

    data.append(x)
    s1 = s1 + x
    s2 = s2 + x*x

pylab.hist(data,bins=100,normed=True)
pylab.show()

print ("Sample mean is",s1/n)
print ("Sample variance is",s2/n-(s1/n)**2)
print (" ")
print ("Sample size is",n)






 
