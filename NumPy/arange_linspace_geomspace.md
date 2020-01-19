## np.arange, np.linspace, np.geomspace
> How do these work?
---

```python
import numpy as np
```
### np.arange

```python
a = np.arange(start=1, stop=10, step=1)
b = np.arange(start=1, stop=10, step=1).reshape((1,9)).T 
c = np.asmatrix(np.arange(start=1, stop=10, step=1)).T 

print(f"None: {a}\nShape: {a.shape}\nNdim: {a.ndim}\n")             
print(f"None: {b}\nShape: {b.shape}\nNdim: {b.ndim}\n")
print(f"None: {c}\nShape: {c.shape}\nNdim: {c.ndim}\n") 
```
__Output__
```python
None: [1 2 3 4 5 6 7 8 9]
Shape: (9,)
Ndim: 1

None: [[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]
 [9]]
Shape: (9, 1)
Ndim: 2

None: [[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]
 [9]]
Shape: (9, 1)
Ndim: 2
```
---

### np.linspace

```python
a = np.linspace(start=1, stop=10, num=9)
b = np.linspace(start=1, stop=10, num=9).reshape((1,9)).T
c = np.asmatrix(np.linspace(start=1, stop=10, num=9)).T

print(f"None: {a}\nShape: {a.shape}\nNdim: {a.ndim}\n")
print(f"None: {b}\nShape: {b.shape}\nNdim: {b.ndim}\n")
print(f"None: {c}\nShape: {c.shape}\nNdim: {c.ndim}\n")
```
Output
```python
None: [ 1.     2.125  3.25   4.375  5.5    6.625  7.75   8.875 10.   ]
Shape: (9,)
Ndim: 1

None: [[ 1.   ]
 [ 2.125]
 [ 3.25 ]
 [ 4.375]
 [ 5.5  ]
 [ 6.625]
 [ 7.75 ]
 [ 8.875]
 [10.   ]]
Shape: (9, 1)
Ndim: 2

None: [[ 1.   ]
 [ 2.125]
 [ 3.25 ]
 [ 4.375]
 [ 5.5  ]
 [ 6.625]
 [ 7.75 ]
 [ 8.875]
 [10.   ]]
Shape: (9, 1)
Ndim: 2
```

### np.geomspace

```python
a = np.geomspace(start=1, stop=10, num=9)
b = np.geomspace(start=1, stop=10, num=9).reshape((1,9)).T
c = np.asmatrix(np.geomspace(start=1, stop=10, num=9)).T

print(f"None: {a}\nShape: {a.shape}\nNdim: {a.ndim}\n")
print(f"None: {b}\nShape: {b.shape}\nNdim: {b.ndim}\n")
print(f"None: {c}\nShape: {c.shape}\nNdim: {c.ndim}\n")
```
Output
```python
None: [ 1.          1.33352143  1.77827941  2.37137371  3.16227766  4.21696503
  5.62341325  7.49894209 10.        ]
Shape: (9,)
Ndim: 1

None: [[ 1.        ]
 [ 1.33352143]
 [ 1.77827941]
 [ 2.37137371]
 [ 3.16227766]
 [ 4.21696503]
 [ 5.62341325]
 [ 7.49894209]
 [10.        ]]
Shape: (9, 1)
Ndim: 2

None: [[ 1.        ]
 [ 1.33352143]
 [ 1.77827941]
 [ 2.37137371]
 [ 3.16227766]
 [ 4.21696503]
 [ 5.62341325]
 [ 7.49894209]
 [10.        ]]
Shape: (9, 1)
Ndim: 2
```
---

### Visualization

```python
import numpy as np
import matplotlib.pyplot as plt


arange = np.arange(start=1, stop=10, step= ((10 - 1) / 50))
linspace =  np.linspace(start=1, stop=10, num=50)
geomspace = np.geomspace(start=1, stop=10, num=50)

func = lambda x: np.cos(x)
plt.plot(func(arange), color='red', label='arange')
plt.plot(func(linspace), color='blue', label='linspace')
plt.plot(func(geomspace), color='green', label='geomspace')
plt.legend()
plt.show()
```

<img src="https://github.com/tmartin2/Miscellaneous/blob/master/images/arange_linspace_geomspace.png" width="600" height="400" align="center" />