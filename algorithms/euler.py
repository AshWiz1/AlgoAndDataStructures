def dfs(a):
    visited[a] = True
    for i in graph[a]:
        if not visited[i]:
            dfs(i)


ts = int(input())

while ts > 0:
    n = int(input())
    cnt = 0
    dic = {}
    graph = [[] for i in range(200)]
    ind = [0] *200
    outd = [0]*200
    visited =[False]*n
    for i in range(n):
        temp = input()
        if temp[0] not in dic:
            dic[temp[0]] = cnt
            cnt+=1
        if temp[-1] not in dic:
            dic[temp[-1]] = cnt
            cnt+=1
        ind[dic[temp[-1]]]+=1
        outd[dic[temp[0]]]+=1

        graph[dic[temp[0]]].append(dic[temp[-1]])
    
    dfs(0)
    flag = True
    for i in visited:
        if not i:
            # print("heyy")
            print("The door cannot be opened.")
            flag = False
            break

    if not flag:
        ts-=1
        continue
    start = -1
    end = -1
    # print(ind)
    # print(outd)
    for i in range(n):
        if ind[i] != outd[i]:
            if ind[i] < outd[i]:
                if start != -1:
                    flag = False
                    break
                else:
                    start = i
            else:
                if end != -1:
                    flag = False
                    break
                else:
                    end = i
    
    if not flag or start == -1 or end == -1:
        print("The door cannot be opened.")
        ts-=1
        continue

    if ind[start]+1 == outd[start] and  ind[end] == outd[end]+1:
        print("Ordering is possible.")

    else:
        print("The door cannot be opened.")
    
    ts-=1