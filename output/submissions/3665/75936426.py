from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    indegree = [0] * (n+1)
    adj_matrix = [[False]*(n+1) for _ in range(n+1)]
    data = list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            adj_matrix[data[i]][data[j]] = True
            indegree[data[j]] += 1
    m = int(input())
    for i in range(m):
        a,b = map(int,input().split())
        if adj_matrix[a][b] == True:
            adj_matrix[a][b] = False
            adj_matrix[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            adj_matrix[a][b] = True
            adj_matrix[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    result = []
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    certain = True
    impossible = False
    for _ in range(n):
        if len(q) == 0:
            impossible = True
            break
        if len(q) >= 2:
            certain = False
            break
        vx = q.popleft()
        result.append(vx)
        for nx in range(1,n+1):
            if adj_matrix[vx][nx] == True:
                indegree[nx] -= 1
                if indegree[nx] == 0:
                    q.append(nx)
    if impossible == True:
        print("IMPOSSIBLE")
    elif certain == False:
        print("?")
    else:
        for i in result:
            print(i,end=' ')
        print()