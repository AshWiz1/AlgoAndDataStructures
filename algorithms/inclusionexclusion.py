import sys
from math import ceil,log,gcd,sqrt


RI = lambda : [int(x) for x in sys.stdin.readline().split()]
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
def YES(): print('Yes')
def NO(): print('No')
INF = 10 ** 18
MOD = 10 ** 9 + 7

def calculate(s,n):
    sign = -1
    n1  = n
    ans = 0
    dic  = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for i in range(1,1<<5):
        # sign = 1
        lcm = 1
        cnt = 0
        for j in range(0,5):
            if (i&(1<<j)):
                cnt+=1
                lcm = lcm*s[j]//gcd(lcm,s[j])
        # dic[cnt].append(lcm)
        if cnt%2 == 1:
            n1 = n1 - n//lcm
        else:
            n1 = n1+n//lcm
        # print(n//lcm)
        # print(bin(i), )
        # ans+=(sign*n//lcm)
    # print(dic)
    return n1


for _ in range(int(ri())):
    n,m,a,d = RI()
    s = []
    for i in range(5):
        s.append(a+i*d)
    # print(s)
    # s=[2]
    # n = 10
    temp1 = calculate(s,m)
    # print(temp1)
    # temp1 = n-temp1
    temp2 = calculate(s,n-1)
    # temp2 = m-1-temp2
    
    print(temp1-temp2)

