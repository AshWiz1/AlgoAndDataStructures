def getsum(BITTree,i): 
    s = 0 
    i = i+1
    while i > 0: 
        s += BITTree[i] 
        i -= i & (-i) 
    return s 

def updatebit(BITTree , n , i ,v): 
    i += 1
    while i <= n: 
        BITTree[i] += v 
        i += i & (-i) 

def construct(arr, n): 
    BITTree = [0]*(n+1) 
    for i in range(n): 
        updatebit(BITTree, n, i, arr[i]) 
    return BITTree 