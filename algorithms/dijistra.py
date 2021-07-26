import sys
from math import gcd
import bisect
import heapq
from collections import deque

# from types import GeneratorType
# def bootstrap(func, stack=[]):
#     def wrapped_function(*args, **kwargs):
#         if stack:
#             return func(*args, **kwargs)
#         else:
#             call = func(*args, **kwargs)
#             while True:
#                 if type(call) is GeneratorType:
#                     stack.append(call)
#                     call = next(call)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     call = stack[-1].send(call)
#             return call
#     return wrapped_function

Ri = lambda : [int(x) for x in sys.stdin.readline().split()]
ri = lambda : sys.stdin.readline().strip()
 
def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
INF = 10 ** 18
MOD = 998244353

for _ in range(int(ri())):
    n,m,u,v = Ri()
    g  = [[] for i in range(n+1)]
    flag = [False]*(n+1)
    for i in range(m):
        x,y,le,sp = Ri()
        time = le/sp
        g[x].append((time,y))
        g[y].append((time,x))
    
    h = []
    heapq.heapify(h)
    heapq.heappush(h,(0,v))
    dist = [INF]*(n+1)
    dist[v] = 0
    while len(h) > 0:  
        cur = heapq.heappop(h)
        cur = cur[1]
        if cur == u:
            break
        flag[cur]  =True
        for i in g[cur]:
             if not flag[i[1]] and dist[cur]+ i[0] < dist[i[1]]:
                 dist[i[1]] = dist[cur]+i[0]
                 heapq.heappush(h,(dist[i[1]],i[1]))
    if dist[u] == INF:
        print(-1)
    else:
        print(dist[u])