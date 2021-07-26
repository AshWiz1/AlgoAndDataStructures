import math

def rangeupdate(ss,se,qs,qe,pos,val):
    if ss == se and qs <= ss and qe >= ss:
        seg[pos] +=val
        return seg[pos]
    
    if se < qs or ss > qe:
        return seg[pos]

    mid = (ss+se)//2
    left = rangeupdate(ss,mid,qs,qe,pos*2+1,val)
    right = rangeupdate(mid+1,se,qs,qe,pos*2+2,val)

    seg[pos] = left+right
    return seg[pos]


def query(ss,se,qs,qe,pos):
    if qs <= ss and qe >= se:
        return seg[pos]

    if qs > se or qe < ss :
        return 0
    mid = (ss+se)//2
    left =  query(ss,mid,qs,qe,pos*2+1)
    right = query(mid+1,se,qs,qe,pos*2+2)

    return left+right

def construct(st,end,pos):
    if st == end:
        seg[pos] = arr[st]
        return seg[pos]

    mid= (st+end)//2
    left = construct(st,mid,2*pos+1)
    right = construct(mid+1,end,2*pos+2)

    seg[pos] = left+right
    return seg[pos]


arr = list(map(int,input().split()))
height = math.ceil(math.log(len(arr),2))

size = 2**(height+1)-1
seg = [0]*size

construct(0,len(arr)-1,0)
print(query(0,len(arr)-1,0,2,0))
rangeupdate(0,len(arr)-1,0,2,0,5)
print(seg)
print(query(0,len(arr)-1,0,2,0))
