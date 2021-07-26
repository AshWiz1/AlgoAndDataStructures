time = 1



def dfs(i,par):
    global time
    visit[i] = True
    time+=1
    tim[i] = time
    low[i] = time

    for j in arr[i]:
        if j == par:
            continue
        if visit[j]:
            low[i] = min(low[i],tim[j])
        else:
            dfs(j,i)
            low[i] = min(low[i],low[j])
            if low[j] > tim[i] :
                ans.append([i+1,j+1])




if  __name__ == "__main__":
    ts = int(input())
    _ =0 
    while _ < ts:
        input()
        time= 1
        n,m = list(map(int,input().split()))
        arr = [[] for i in range(n)]
        visit = [False]*n
        ans = []
        low = [-1]*n
        tim = [-1]*n
        for i in range(m):
            a,b = list(map(int,input().split()))
            a-=1
            b-=1
            # print(arr)
            arr[a].append(b)
            arr[b].append(a)

        for i in range(n):
            if not visit[i]:
                dfs(i,-1)
        # ans.sort(key=lambda x: (x[1], x[0]))
        ans = ans[::-1]
        print("Caso #"+str(_+1))
        if len(ans) > 0:
            
            print(len(ans))
            for temp in ans:
                print(temp[0],temp[1])
        else:
            print("Sin bloqueos")
        _+=1