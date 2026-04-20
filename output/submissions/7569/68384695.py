import sys
input = sys.stdin.readline
from collections import deque

INF = int(1e9)
m, n, h = map(int,input().split())
box = [ []for _ in range(h)]
visited = [[ [INF]*m for _ in range(n)] for _ in range(h)]
for i in range(n*h):
    tmp = list(map(int,input().split()))
    box[i//n].append(tmp)
t = []
to_x = []
to_y = []
to_z = []
answer = 0

def bfs(array,x,y,z):
    l = len(x)
    for i in range(l):
        visited[x[i]][y[i]][z[i]] = 0
    queue_x = deque(x)
    queue_y = deque(y)
    queue_z = deque(z)
    dx = [0,0,1,-1,0,0]
    dy = [1,-1,0,0,0,0]
    dz = [0,0,0,0,1,-1]
    while queue_x:
        vx = queue_x.popleft()
        vy = queue_y.popleft()
        vz = queue_z.popleft()
        for i in range(6):
            nx = vx + dx[i]
            ny = vy + dy[i]
            nz = vz + dz[i]
            if nx >=0 and ny >= 0 and nx < h and ny < n and nz < m and 0 <= nz :
                if visited[nx][ny][nz] > visited[vx][vy][vz] + 1:
                    visited[nx][ny][nz] = visited[vx][vy][vz] + 1
                    if array[nx][ny][nz] == 0:
                        queue_x.append(nx)
                        queue_y.append(ny)
                        queue_z.append(nz)
    

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                to_x.append(i)
                to_y.append(j)
                to_z.append(k)
            elif box[i][j][k] == 0:
                t.append((i,j,k))

bfs(box, to_x, to_y, to_z)

for i in t:
    if visited[i[0]][i[1]][i[2]] == INF:
        answer = -1
        break
    else:
        answer = max(answer,visited[i[0]][i[1]][i[2]])

if t == []:
    answer = 0
print(answer)