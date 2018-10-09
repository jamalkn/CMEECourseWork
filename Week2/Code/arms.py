"""
Created on Tue Feb 03 18:43:51 2015

@author: Jamal Khan
"""
import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg as LA
from scipy import integrate
import scipy


N = 10
alpha = 3
total = 5000

elements = [-1, 1]
probabilities = [0.5, 0.5]
sum1 = 0; sum2 = 0; sum3 = 0; sum4 = 0; n1 = 0
h1 = 0; h2 = 0
z = []
l = math.sqrt(2*N)
n1 = N*(N+1)*total/2
data = []

f = lambda x : 1/((1+(math.tan(x))**(alpha+1))*((math.cos(x))**2))
y = scipy.integrate.quad(f, 0, math.pi/2)
k = 1/2/y[0] #k is the normalisation constant


f = lambda x : (k*(math.tan(x)))/((1+(math.tan(x))**(alpha+1))*((math.cos(x))**2))
if alpha > 1:
    y = scipy.integrate.quad(f, 0, math.pi/2)
    e1 = 2*y[0]
    print("e1 = ",e1)


f = lambda x : (k*(math.tan(x))**2)/((1+(math.tan(x))**(alpha+1))*((math.cos(x))**2))
if alpha > 2:
    y = scipy.integrate.quad(f, 0, math.pi/2)
    e2 = 2*y[0]
    print("e2 = ",e2)


f = lambda x : (k*(math.tan(x))**3)/((1+(math.tan(x))**(alpha+1))*((math.cos(x))**2))
if alpha > 3:
    y = scipy.integrate.quad(f, 0, math.pi/2)
    e3 = 2*y[0]
    print("e3 = ",e3)


f = lambda x : (k*(math.tan(x))**4)/((1+(math.tan(x))**(alpha+1))*((math.cos(x))**2))
if alpha > 4:
    y = scipy.integrate.quad(f, 0, math.pi/2)
    e4 = 2*y[0]
    print("e4 = ",e4)

f = lambda x : k/((1+(math.tan(x))**(alpha+1))*((math.cos(x))**2))

for r in range(0, total):
    n = np.zeros((N,N))

    for w in range(0, N):
        x = 0
        u = 0.5 + 0.5 * random.uniform(0, 1.0)
        t0 = 0; t1 = 0; t2 = 0

        while True:
            tn = math.atan(t0)
            y = scipy.integrate.quad(f, 0, tn)
            s = y[0]
            s1 =  k/(1 + t0**(alpha + 1))
            t1 = t1 - (s + 0.5 - u)/s1
            t2 = t0
            t0 = t1
            if abs(t2-t1)<0.000001:
                break

        x = t1*np.random.choice(elements, p=probabilities)/math.sqrt(N)
        n[w,w] = x
        sum1 = sum1 + abs(x); sum2 = sum2 + x*x; sum3 = sum3 + abs(x**3); sum4 = sum4 + x**4


    for v in range(1,N):
        for w in range(0, N-v):
            x = 0
            u = 0.5 + 0.5 * random.uniform(0, 1.0)
            t0 = 0; t1 = 0; t2 = 0
            
            while True:
                tn = math.atan(t0)
                y = scipy.integrate.quad(f, 0, tn)
                s = y[0]
                s1 =  k/(1 + t0**(alpha + 1))
                t1 = t1 - (s + 0.5 - u)/s1
                t2 = t0
                t0 = t1
                if abs(t2-t1)<0.000001:
                    break
            
            x = t1*np.random.choice(elements, p=probabilities)/math.sqrt(N)
            n[w,w+v] = x
            n[w+v,w] = n[w,w+v]
            sum1 = sum1 + abs(x); sum2 = sum2 + x*x; sum3 = sum3 + abs(x**3); sum4 = sum4 + x**4

#        if abs(math.floor(v/10)-v/10)< 0.00001:
#            t1 = t1*1
#            print (v)

    e_vals = LA.eigvalsh(n)
    z.extend(e_vals)
    h = 0
    for ia in range(0,N):
        if abs(e_vals[ia])>2:
            h = h + 1
    h1 = h1 + h
    h2 = h2 + h*h

    if abs(math.floor(r/100)-r/100)< 0.00001:
        t1 = t1*1
        print (r)
    #print(r)


z = np.asarray(z)
plt.hist(z, normed=True, bins=100, range = (-5,5))

#h1 = 0
#for i in range(0,total*N):
#    if abs(z[i])>2:
#        h1 = h1 + 1

print (" ")
print ("alpha = ",alpha)
print ("The matrix size N is",N)
print ("Number of random matrices is",total)
print ("Number of random variates is",n1)

if alpha > 1:
    print ("Sample mean of ||x|| is",sum1/n1,  " [Expected value =", e1/math.sqrt(N),"]")
else:
    print ("Sample mean of ||x|| is",sum1/n1,  " [Expected value does not exist]")

if alpha > 2:
    print ("Sample mean of x**2 is",sum2/n1,  " [Expected value =", e2/N,"]")
else:
    print ("Sample mean of ||x|| is",sum2/n1,  " [Expected value does not exist]")

if alpha > 3:
    print ("Sample mean of ||x||**3 is",sum3/n1,  " [Expected value =", e3/math.sqrt(N**3),"]")
else:
    print ("Sample mean of ||x||**3 is",sum3/n1,  " [Expected value does not exist]")
        
if alpha > 4:
    print ("Sample mean of x**4 is",sum4/n1," [Expected value =", e4/N**2,"]")
else:
    print ("Sample mean of x**4 is",sum4/n1," [Expected value does not exist]")

print ("The minimum eigenvalue is ", min(z))
print ("The maximum eigenvalue is ", max(z))
print ("Sum of # is ", h1)
print ("Sum of #**2 is", h2)
print ("Sample variance =",(h2-(h1**2)/total)/(total-1))

