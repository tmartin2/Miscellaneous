import numpy as np
from typing import List, Tuple
from itertools import combinations as comb


__author__ = 'Trevor Martin'


def compute_optimal(p: List[int], s: List[int], m: int, C: int) -> int:
    n = len(p)
    memo = [0 for i in range(n)]
    memo[0], memo[1] = 0, (s[1] - C) 
    for i in range(2,n):
        memo[i] = s[i] - C + max([memo[i - x] for x in range(1,m+1)])
    return memo[n-1]


def compute_route(p: List[int], s: List[int], m: int, C: int) -> List[int]:
    n = len(p)
    p_s = list(zip(p,s))
    routes = [list(comb(p_s, x)) for x in range(2,n)]
    valid = [subsub for sub in routes for subsub in sub if (subsub[0]==p_s[0] and subsub[-1]==p_s[-1])]
    routes_diffs = lambda route: [pond[0] - route[index-1][0] if pond else None for index, pond in enumerate(route)][1:] 
    valid2 = [route for route in valid if max(routes_diffs(route)) <= m]
    summate = lambda route: np.sum(np.asarray([s_i[1] for s_i in route]))
    total_s = [summate(route)-(len(route)*C) for route in valid2]
    return valid2[total_s.index(max(total_s))] 
    

def main():
    
    # Example 1
    ponds = [0,1,2,3,4,5,6] 
    shrimps = [0,3,4,2,1,3,2]
    m = 3
    C = 1
    opt = compute_optimal(ponds, shrimps, m, C)
    print(opt) # we get 9
    r = compute_route(ponds, shrimps, m, C)
    print(r)
    
    # Example 2
    ponds = [0,1,2,3,4,5]
    shrimps = [0,1,1,1,100,1]
    m = 2
    C = 20
    opt = compute_optimal(ponds, shrimps, m, C)
    print(opt) # we get 42
    r = compute_route(ponds, shrimps, m, C)
    print(r)
    
    # Example 3                                                                
    ponds = [0,1,2,3,4,5]
    shrimps = [0,100,1,1,100,1]
    m = 2
    C = 20
    opt = compute_optimal(ponds, shrimps, m, C)
    print(opt) # we get 122
    r = compute_route(ponds, shrimps, m, C)
    print(r)

    # Example 4                                                                
    ponds = [0,1,2,3]
    shrimps = [0,3,1,1]
    m = 3
    C = 1
    opt = compute_optimal(ponds, shrimps, m, C)
    print(opt) # we get 2
    r = compute_route(ponds, shrimps, m, C)
    print(r)
    
    # Example 5         
    np.random.seed(1234)
    ponds = list(range(20))
    shrimps = list(range(1)) + list(np.random.randint(low=5, high=18, size=20))
    m = 5
    C = 15
    print(f"Ponds:{ponds}\nShrimps:{shrimps}\nm:{m}\nC:{C}")
    opt = compute_optimal(ponds, shrimps, m, C)
    print(opt) # we get 42
    r = compute_route(ponds, shrimps, m, C)
    print(r)

if __name__ == '__main__':
    main()
