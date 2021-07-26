import sys
# from math import ceil,log,gcd,sqrt
# sys.setrecursionlimit(10**9)

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


# ans = []

def dfs(x):
    if not visit[x]:
        visit[x] = True
        for i in range(n):
            if lis[x][i] :
                dfs(i)
        top.append(x)


n,m = RI()
lis = list2d(n,n,False)
for i in range(m):
    temp = RI()
    for j in range(1,temp[0]+1):
        lis[temp[j]-1][i] = True
# for i in lis:
#     print(*i)
visit = [False]*n
top = []
for i  in range(n):
    if not visit[i]: 
        dfs(i) 
        # top.append(i)

# print(*top)
pre  = -1
par = [-1]*n
for i in range(len(top)):
    temp = top[i]
    par[temp] = pre
    pre= temp
par = [i+1 for i in par]
s = []
for i in par:
    s.append(str(i))
    s.append('\n')
sys.stdout.write("".join(s))