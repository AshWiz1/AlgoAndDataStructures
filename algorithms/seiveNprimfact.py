# cook your dish here
import sys
import math
#  if (ans[i-1]+1)%3 == 0 else (ans[i-1]+1)%3

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
def YES(): print('YES')
def NO(): print('NO')
INF = 10 ** 18
MOD = 10 ** 9 + 7


#sieve and getting minimun prime factor of each number and using it to cal prime factorization.
def seive():
    p= 2
    while (p*p < 10005):
        if prime[p]:
            for i in range(p*p,10005,p):
                if prime[i]:
                    prime[i]=not prime[i]
                    sp[i] = p
        p+=1

for _ in range(int(ri())):
    n,m = RI()
    a= RI()

    prime = [True]*(10005)
    sp = [i for i in range(0,10005)]
    seive()
    dic = {}
    for i in a:
        while(i > 1):
            temp = sp[i]
            cnt = 0
            while(i%temp == 0): cnt+=1;i=i//temp
            if temp  in dic:
                dic[temp]  = max(dic[temp],cnt)
            else:
                dic[temp] = cnt
    maxx = 1
    maxnum = 1
    for i in range(2,m+1):
        tempp = i
        tempmax = 1
        while(i > 1):
            temp = sp[i]
            cnt = 0
            while (i%temp == 0): cnt+=1;i=i//temp
            if temp in dic:
                if cnt > dic[temp]:
                    tempmax*=(temp**(cnt-dic[temp]))
            else:
                tempmax*=(temp**cnt)
        if tempmax > maxx:
            maxx = tempmax
            maxnum = tempp
    print(maxnum)