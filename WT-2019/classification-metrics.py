"""Rudimentary Classification Metrics                                                                    

Author: Trevor Martin                                                                                                              
Date: 15 January 2020                                                                                                              
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


def main():

    np.random.seed(3) 

    # low[, high, size, dtype]
    rand_size = lambda: np.random.randint(low=25, high=100)
    rand_dist = lambda: np.random.randint(low=1, high=100, size=rand_size())
    
    true_positive, true_negative = rand_dist, rand_dist
    false_positive, false_negative = rand_dist, rand_dist

    plt.plot(true_positive, color='red', label='TP')
    plt.plot(true_negative, color='blue', label='TN')
    plt.plot(false_positive, color='green', label='FP')
    plt.plot(false_negative, color='orange', label='FN')

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
