"""Softmax Function

Author: Trevor Martin
Date: 15 January 2020
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d


def main():
    
    vecs = np.array([[5, 1, 2],
                     [3, 3, 1],
                     [4, 3, 6],
                     [2, 3, 5]])

    
    softmax = lambda vector: [np.exp(vector)/float(np.sum(np.exp(vector)))]
    apply_soft = np.asarray([softmax(vec) for vec in vecs])

    print(f"SOFT: {apply_soft}")
    
    figure = plt.figure()
    axes = figure.add_subplot(111, projection='3d')
    axes.plot(vectors[0],
              vectors[1],
              vectors[2],
              'o', color="red")
    axes.plot(apply_soft[0],
              apply_soft[1],
              apply_soft[2],
              'o', color="blue")

    #array = np.arange(start=-10, stop=11, step=1)
    #soft_array = softmax(array)
    #plt.plot(soft_array) 
    
    plt.show()
    
if __name__ == '__main__':
    main()
