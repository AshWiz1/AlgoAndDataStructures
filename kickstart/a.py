import sys
from math import log2,floor,ceil,sqrt


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



for _ in range(int(ri())):
    n,k = Ri()
    a = Ri()
    i = 0
    cnt = 0
    while (i < n):
        j = i
        if a[i] == k:
            # print(i)
            ite = k
            flag = False
            # j = 0
            for j in range(i,n):
                if a[j] != ite:
                    flag  = False
                    break
                if ite == 1:
                    flag = True
                    break
                ite-=1
            if flag : 
                cnt+=1
            if j != i:
                i = j
            else:
                i+=1
        else:
            i+=1
        # i = j


    print("Case #%d: %d" % (_+1,cnt))