import bisect

def precompute(n):
    # print(n)
    result = 1
    temp = 0
    while n%2 == 0:
        n/=2
        temp+=1
    result = temp*2 +1
    if(result >= 10000):
	    return -1
    i=3
    while i*i <= n:
        
        temp = 0
        while n%i == 0:
            n/=i
            temp+=1
        
        result*=(temp*2+1)
        if result >= 10000 :
            return -1
        i+=2

    if n != 1:
        result*=3
    return result
        

arr= [[] for i in range(100000)]

for i in range(1,100001):
    ret = precompute(i)
    if ret > 0:
        arr[ret].append(i*i)

# print(arr[5])

q = int(input())
while q > 0:
    k,a,b = list(map(int,input().split()))
    # print(arr[k])
    temp1 = bisect.bisect_left(arr[k], a, lo=0, hi=len(arr[k]))
    temp2 = bisect.bisect_right(arr[k], b, lo=0, hi=len(arr[k]))
    print(temp2-temp1)
    q-=1