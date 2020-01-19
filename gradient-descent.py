"""Gradient Descent

A NumPy implementation of the gradient descent algorithm

Author: Trevor Martin
Date: 11 January 2020
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


# Describe gradient descent mathematically (hand worked out examples) with Latex examples
# Show gradient descent programmatically in base python and numpy, with matplotlib animations
# For both vector and scalar input for different functions
# Do this all in Jupyter Notebooks

# vector valued input; w is a 1xN vector
function1 = lambda w: -np.cos(np.radians(2*np.pi*w.T*w)) + w.T*w

#w = [np.asmatrix(np.lin)] 
#figure = plt.figure()
#axes = figure.add_subplot(111, projection='3d')
#axes.plot([1,2,3], [3,2,1], [5,6,7])
#plt.show()

# scalar input; w is a scalar
#function2 = lambda w: np.log(1 + np.exp(1)**(w**2))
#w = np.linspace(start=-1, stop=1, num=50)
#fig = plt.figure()
#axes = fig.add_subplot(111, projection='2d')
#plt.plot(np.linspace(-1,1), function2(w))

#def descent(alpha, func):
#    w_init = 0.3
#    deriv_f2 = lambda w: (2*(np.exp(1)**(w**2))*w) / (1 + np.exp(1)**(w**2))
#    for step in range(10):
#        plt.plot(w_init, func(w_init), marker='o', color='red')
#        step_point = deriv_f2(w_init) - alpha
#        w_init = func(step_point)
#    plt.show()
    #for step in steps:
#descent(0.01, function2)        

#plt.close()



# function2_ = lambda w, x: (1 / (1 + np.exp(x)**(w**2))) * np.exp(x)**(w**2) * (2*w)
# function2_ = lambda w, x: sym.diff(lambda w, x: np.log(1 + np.exp(x)**(w**2)),(w,x)) 

# plt.plot(function2(np.linspace(-1, 1, 50), np.linspace(-1, 1, 50)), np.linspace(0.5, 1.5, 50))
# plt.plot(function2(np.linspace(-10,10, 50)), np.linspace(0.5, 1.5, 50))
#plt.show() 

# NP.ARANGE v. NP.LINSPACE v. NP.GEOMSPACE
#plt.plot(function(np.asmatrix(np.linspace(start=-10, stop=10, num=5))))
#plt.show()
#plt.plot(function(np.asmatrix(np.linspace(start=-10, stop=10, num=5))))
#plt.show()

# USING NP.ARANGE
a = np.geomspace(start=1, stop=10, num=9)
b = np.geomspace(start=1, stop=10, num=9).reshape((1,9)).T
c = np.asmatrix(np.geomspace(start=1, stop=10, num=9)).T

print(f"None: {a}\nShape: {a.shape}\nNdim: {a.ndim}\n")
print(f"None: {b}\nShape: {b.shape}\nNdim: {b.ndim}\n")
print(f"None: {c}\nShape: {c.shape}\nNdim: {c.ndim}\n")

arange = np.arange(start=1, stop=10, step= ((10 - 1) / 50))
linspace =  np.linspace(start=1, stop=10, num=50)
geomspace = np.geomspace(start=1, stop=10, num=50)

func = lambda x: np.cos(x)
plt.plot(func(arange), color='red', label='arange')
plt.plot(func(linspace), color='blue', label='linspace')
plt.plot(func(geomspace), color='green', label='geomspace')
plt.legend()
plt.show()

#plt.plot(function(np.asmatrix(np.arange(-1,1,0.01))))
#plt.show()


