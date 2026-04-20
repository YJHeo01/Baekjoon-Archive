from collections import deque

INF = 1000001
n, m = map(int,input().split())
array = []
visited = [[INF]*m for _ in range(n)]
x,y= 0,0
for i in range(n):
    tmp = list(map(int,input().split()))
    array.append(tmp)
    for j in range(m):
        if tmp[j] == 2:
            x,y = i,j

def bfs(start_x,start_y):
    queue_x = deque([start_x])
    queue_y = deque([start_y])
    visited[start_x][start_y] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue_x:
        vx = queue_x.popleft()
        vy = queue_y.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
 
            if array[nx][ny] == 1:
                if visited[nx][ny] == INF:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue_x.append(nx)
                    queue_y.append(ny)
            else:
                visited[nx][ny] = 0
bfs(x,y)
for i in range(n):
    for j in range(m):
        if visited[i][j] == INF:
            if array[i][j] == 1:
                print("-1",end=' ')
            else:
                print("0",end=' ')
        else:
            print(visited[i][j],end=' ')
    print("")