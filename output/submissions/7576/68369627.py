from collections import deque

def bfs(array,visited,x,y,m,n):
    cnt = 1
    visited[x][y] = 0
    queue_x = deque([x])
    queue_y = deque([y])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue_x:
        vx = queue_x.popleft()
        vy = queue_y.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx >=0 and ny >= 0 and nx < n and ny < m:
                if visited[nx][ny] >= visited[vx][vy] + 1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    cnt = visited[nx][ny]
                    if array[nx][ny] == 0:
                        queue_x.append(nx)
                        queue_y.append(ny)
    return cnt
    
INF = int(1e9)
m, n = map(int,input().split())
box = []
visited = [ [INF]*m for _ in range(n)]
for i in range(n):
    tmp = list(map(int,input().split()))
    box.append(tmp)
t = []
answer = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tmp = bfs(box,visited,i,j,m,n)
        elif box[i][j] == 0:
            t.append((i,j))

for i in t:
    if visited[i[0]][i[1]] == INF:
        answer = -1
        break
    else:
        answer = max(answer,visited[i[0]][i[1]])

if t == []:
    answer = 0
print(answer)