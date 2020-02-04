"""Sigmoid Function

Author: Trevor Martin
Data: 16 January 2020
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d # need for projection="3d"


def main():
    
    vectors = np.array([[1, 2, 3],
                        [2, 5, 4],
                        [4, 3, 3]])

    sigmoid = lambda vector: [float(1 / (1 + np.exp(-x))) for x in vector]
    apply_sig = np.asarray([sigmoid(vec) for vec in vectors])

    figure = plt.figure()
    axes = figure.add_subplot(111, projection='3d')
    axes.plot(vectors[0],
              vectors[1],
              vectors[2],
              'o', color="red")
    axes.plot(apply_sig[0],
              apply_sig[1],
              apply_sig[2],
              'o', color="blue")
    plt.show()
    
if __name__ == '__main__':
    main()
