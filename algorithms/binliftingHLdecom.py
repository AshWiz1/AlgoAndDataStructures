import sys
from math import ceil,log2
# sys.setrecursionlimit(10**5)

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
MOD = 10 ** 9 + 7
LIMIT = 10**6+2

def dfs(cur,par):
    mem[cur][0] = par
    subsize[cur] = 1
    for i in range(1,log+1):
        mem[cur][i] = mem[mem[cur][i-1]][i-1]
    for i in g[cur]:
        if i != par:
            lev[i] =lev[cur]+1
            dfs(i,cur)
            subsize[cur]+=subsize[i]

def lcaa(u,v):
    if lev[u] < lev[v]:
        u,v = v,u
    # print(u,v)
    for i in range(log,-1,-1):
        if lev[u]-pow(2,i) >= lev[v]:
            # print("sf")
            u = mem[u][i]
    # print(u)
    if u ==v:
        return u
    for i in range(log,-1,-1):
        if mem[u][i] != mem[v][i]:
            u = mem[u][i]
            v = mem[v][i]
    return mem[u][0]

def combine(dic1,dic2):
    dic3 = {**dic1, **dic2}
    for key, value in dic3.items():
        if key in dic1 and key in dic2:
            dic3[key] = dic1[key]+dic2[key]
 
    return dic3

def seive():
    p= 2
    while (p*p < LIMIT):
        if prime[p]:
            for i in range(p*p,LIMIT,p):
                if prime[i]:
                    prime[i]=not prime[i]
                    sp[i] = p
        p+=1
def primefact(i):
    dic = {}
    while(i > 1):
            temp = sp[i]
            cnt = 0
            while(i%temp == 0): cnt+=1;i=i//temp
            dic[temp] = cnt
    return dic

def hld(cur,par):
    global chainno
    global ite
    arrayt[ite] = cur
    indexinarray[cur] = ite
    ite+=1
    # print(cur)
    if(chainhead[chainno] == -1): chainhead[chainno] = cur;
    chainind[cur] = chainno
    chainpos[cur] = chainsize[chainno]
    chainsize[chainno]+=1

    ind = -2;main = -1
    for i in g[cur]:
        if i!= par and subsize[i] > main:
            main = subsize[i]
            ind = i
    if ind >= 1: hld(ind,cur)

    for i in g[cur]:
        if i != ind and  i!= par:
            chainno+=1
            hld(i,cur)

def hldq(u,v):
    dic = {}
    global n
    while True:
        if chainind[u] == chainind[v]:
            l = indexinarray[u]
            r = indexinarray[v]
            dic = combine(dic,tq(l,r,0,n-1,0))
            return dic

        head = chainhead[chainind[v]]
        l = indexinarray[head]
        r = indexinarray[v]

        dic = combine(dic,tq(l,r,0,n-1,0))
        v = mem[head][0]

def buildt(lo,high,pos):
    if lo == high:
        segt[pos] = a[arrayt[lo]].copy()
        # print(segt)
        return segt[pos]
    mid = (lo+high)//2
    dic1 = buildt(lo,mid,2*pos+1)
    dic2 = buildt(mid+1,high,2*pos+2)
    segt[pos] = combine(dic1,dic2)
    # print(segt)
    return segt[pos]
    # print(pos,segt[pos],segt[2*pos+1],segt[2*pos+2])

def tq(l,r,lo,high,pos):
    if l > high or r < lo:
        return {}
    if l<=lo and r>=high : return segt[pos]
    mid = (lo+high)//2
    dic1 = tq(l,r,lo,mid,2*pos+1)
    dic2 = tq(l,r,mid+1,high,2*pos+2)
    return combine(dic1,dic2)

prime = [True]*(LIMIT)
sp = [i for i in range(0,LIMIT)]
seive()
for _ in range(int(ri())):
    #hld and segment treee stuff

    n = int(ri())
    #hld stuff -----------------------
    subsize = [0]*(n+1)
    chainno = 0
    chainhead = [-1]*(n+1)
    chainpos = [-1]*(n+1)
    chainind = [-1]*(n+1)
    chainsize = [0]*(n+1)
    indexinarray = [0]*(n+1)
    arrayt = [0]*(n+1)
    segt=  [{}]*(4*n +1)

    ite=0
    #hld--------------------------------
    g = [[] for i in range(n+1)]
    log = ceil(log2(n))
    mem = list2d(n+1,log+1,0)
    lev = [0]*(n+1)
    for i in range(n-1):
        a,b = Ri()
        g[a].append(b)
        g[b].append(a)
    dfs(1,1)
    hld(1,1)
    # print(arrayt)
    a= Ri()
    a = [0]+a
    for i in range(1,len(a)):
        a[i] = primefact(a[i])
    # for i in arrayt:
    #     print(a[i],end=" ")
    # print()
    # print(a)
    buildt(0,n-1,0)
    # print(segt)
    # print(a)
    # print(tq(2,3,0,n-1,0))
    for qq in range(int(ri())):
        s,e = Ri()
        lca = lcaa(s,e)
        dic1 = hldq(lca,s)
        dic2 = hldq(lca,e)
        # print(dic1,dic2)
        dic1=  combine(dic1,dic2)
        for i in a[lca]:
            dic1[i]-=a[lca][i]
        ans=1
        for i in dic1:
            ans*=(dic1[i]+1)
            ans=ans%MOD
        print(ans)

    