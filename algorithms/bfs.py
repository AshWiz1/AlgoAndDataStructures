import math

ts = int(input())

while ts > 0:
    n = int(input())
    graph = [ [] for i in range(n)]
    ans=  -1

    def bfs(i):
        global ans
        que = []
        que.append(i)
        visit = [False]*n
        dist = [0]*n

        while(len(que) > 0):
            temp = que.pop(0)
            visit[temp] = True
            for j in graph[temp]:
                if not visit[j]:
                    que.append(j)
                    dist[j] = dist[temp]+1

        index = 0
        maxx = -1
        for i in range(len(dist)):
            if maxx < dist[i]:
                index = i
                maxx = dist[i]

        ans = maxx+1
        return index

    for i in range(n-1):
        a,b = list(map(int,input().split()))

        graph[a].append(b)
        graph[b].append(a)

    bfs(bfs(0))
    print(math.ceil(ans/2))
    ts-=1