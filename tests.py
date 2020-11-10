import line_profiler
import itertools as it
import numpy as np

@profile
def test_one():
    return it.accumulate([1,2,3])

@profile
def test_two():
    return np.cumsum(np.array([1,2,3])).tolist()

if __name__ == '__main__':
    test_one()
    test_two()

'''
@profile
def test_one():
    return list(it.accumulate([1,2,3]))

@profile
def test_two():
    return np.cumsum(np.array([1,2,3])).tolist()

if __name__ == '__main__':
    test_one()
    test_two()

Wrote profile results to tests.py.lprof
Timer unit: 1e-06 s

Total time: 5e-06 s
File: tests.py
Function: test_one at line 5

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     5                                           @profile
     6                                           def test_one():
     7         1          5.0      5.0    100.0      return it.accumulate([1,2,3])

Total time: 2.9e-05 s
File: tests.py
Function: test_two at line 9

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     9                                           @profile
    10                                           def test_two():
    11         1         29.0     29.0    100.0      return np.cumsum(np.array([1,2,3])).tolist()

RESULTS: USE NP.CUMSUM NOT IT.ACCUMULATE()
'''

# kernprof -l -v your_code.py

'''
@profile
def test_mul():
    return operator.__mul__([1], 10)

@profile
def test_list():
    return [1 for i in range(10)]

@profile
def test_list2():
    return [1]*10

if __name__ == '__main__':
    test_mul()
    test_list()
    test_list2()

Total time: 4e-06 s
File: tests.py
Function: test_mul at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def test_mul():
     6         1          4.0      4.0    100.0      return operator.__mul__([1], 10)

Total time: 3e-06 s
File: tests.py
Function: test_list at line 8

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     8                                           @profile
     9                                           def test_list():
    10         1          3.0      3.0    100.0      return [1 for i in range(10)]

Total time: 1e-06 s
File: tests.py
Function: test_list2 at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           @profile
    13                                           def test_list2():
    14         1          1.0      1.0    100.0      return [1]*10


RESULT: DONT USE operator.__mul__()
'''
