## np.arange, np.linspace, np.geospace
> How do these work?
---

### np.arange

```python
a = np.arange(start=1, stop=10, step=1)
b = np.arange(start=1, stop=10, step=1).reshape((1,9)).T 
c = np.asmatrix(np.arange(1, 10, 1)).T 

print(f"None: {a}\nShape: {a.shape}\nNdim: {a.ndim}\n")                                                        
print(f"None: {b}\nShape: {b.shape}\nNdim: {b.ndim}\n")                                                        
print(f"None: {c}\nShape: {c.shape}\nNdim: {c.ndim}\n") 
```
Outuput
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