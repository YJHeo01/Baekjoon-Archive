from collections import deque
n,m = map(int,input().split())
safe = 0
virus = []
array = []
for i in range(n):
    tmp = tuple(map(int,input().split()))
    array.append(tmp)
    for j in range(m):
        if tmp[j] == 2:
            virus.append((i,j))
def bfs(g,virus,a,b,c):
    graph = []
    for i in range(n):
        graph.append(list(g[i]))
    graph[a[0]][a[1]] = 1
    graph[b[0]][b[1]] = 1
    graph[c[0]][c[1]] = 1
    queue = deque(virus)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 0
    while queue:
        v = queue.popleft()
        graph[v[0]][v[1]] = 2
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = 2
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt
for i in range(n*m-2):
    for j in range(i+1,n*m-1):
        for k in range(j+1,m*n):
            if array[i//m][i%m] != 0 or array[j//m][j%m] != 0 or array[k//m][k%m] != 0:
                continue 
            s = bfs(array,virus,(i//m,i%m),(j//m,j%m),(k//m,k%m))
            safe = max(s,safe)

print(safe)