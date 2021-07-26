import sys
# import bisect
# from collections import deque

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
MOD = 10**9+7

def getBase3Num(num, n, p):
    arr = []
    for i in range(n):
        arr.append(num%p)
        num=num//3
    return arr

for _ in range(int(ri())):
    n,p = Ri()
    par = Ri()
    c = Ri()
    cnt = 0

    g = [[] for i in range(n)]
    for i in range(n-1):
        g[par[i]-1].append(i+1)

    def dfs(cur, arr):
        summ = 0
        for child in g[cur]:
            summ+=dfs(child, arr)
        return summ+arr[cur]

    def check(arr):
        for i in range(n):
            val = 0
            branches = []
            for j in g[i]:
                branches.append(dfs(j, arr))
            tot = sum(branches)+arr[i]
            for j in branches:
                val += j*(tot-j)
            val+= arr[i]*tot
            val = val%p
            if val != c[i]:
                return False
        return True

    ans = []
    for i in range(p**n):
        arr = getBase3Num(i, n, p)
        if check(arr):
            ans = arr[:]
            cnt+=1
    if cnt == 0:
        print(0)
        print(-1)
    else:
        print(cnt)
        print(" ".join(map(str, ans)))