import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(334234)

'''
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
fig, ax1 = plt.subplots(figsize=(6,6),
                        subplot_kw={'projection':'3d'})
g = lambda w: w.T*w + 2
b = np.linspace(-0.8,0.8,100)
c = np.linspace(-5,5,20).reshape(-1,1)
#y = g(np.linspace(-5,5,20).reshape(-1,1))
x, y = np.meshgrid(b,b) 
z = g(x + y)
#z = (1 / (1 + np.exp(-(x**2 + y**2)))) 
ax1.plot_wireframe(x,y,z)
#surf = ax.plot_surface(x, y, z.reshape(-1,1), cmap=cm.coolwarm, 
#                       linewidth=0, antialiased=False)
plt.show()
#z = g(np.linspace(-5, 5, 100))
#N = 3
# x = np.linspace(-5, 5, 100).reshape(3, -1)
'''

alpha = 0.5  # steplength
N = 3 # dimensionality of vectors
P = 5 # num random direction about each point to search
steps = 12 # num local optimization steps
w = np.array([[3],[4]]) # a column vector to begin the search
g = lambda w: w.T*w + 2 # func g that takes in a col vector

for step in range(steps):
    try:
        # I want it to have 5 columns, add -1 to make it compute the rows on its own
        directions = [np.random.uniform(-1, 1, N).reshape(N, -1) for _ in range(P)]
        valid_dirs = []
        print(g(w),  g(w+np.full((N, 1), dir)))
        for dir in directions:
            if np.greater_equal(g(w),  g(w+np.full((N, 1), dir))).all():
                valid_dirs.append(dir)
        opt_dir = np.array([min(list(it.chain.from_iterable(valid_dirs)))])
        w = w + direction
        print(w)
    except ValueError:
        continue





'''
g = lambda w: w.T*w + 2

x = np.linspace(-5, 5, 100)
y = g(x)

# the curve
plt.plot(x, y, color='black')

w = np.array([4])


num_steps = 40
num_searches = 40

for step in range(num_steps):
    try:
        plt.scatter(w, 0, s=4, c='red')
        plt.scatter(w, g(w), s=8, c='red')
        d = [np.random.uniform(-1, 1, 1) for _ in range(num_searches)]
        valid_dirs = []
        for direction in d:
            if g(w) > g(w+direction):
                valid_dirs.append(direction)
        best_dir = np.array([min(list(it.chain.from_iterable(valid_dirs)))])
        w = w + best_dir
        print(w)
    except ValueError:
        continue
plt.show()
'''
