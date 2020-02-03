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

#figure = plt.figure()
#axes = figure.add_subplot(111, projection='3d')

# scalar input; w is a scalar
function2 = lambda w: np.log(1 + np.exp(1)**(w**2))
w = np.linspace(start=-1, stop=1, num=50)
plt.plot(w, function2(w))

#fig = plt.figure()
#axes = fig.add_subplot(111, projection='2d')
#plt.p

def descent(alpha, func):

    w_init = 1

    deriv_f2 = lambda w: (2 * (np.exp(1)**(w**2)) * w) / (1 + np.exp(1)**(w**2))

    for step in range(0,100):

        plt.plot(w_init, func(w_init), marker='o', color='red')

        #step_point = 2deriv_f2(w_init)

        #w_init = func(step_point)
        w_init = alpha*deriv_f2(w_init)
    plt.show()

descent(0.001, function2)        

#plt.close()
