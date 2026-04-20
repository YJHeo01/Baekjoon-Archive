from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

def bfs(array,visited,x,y,z,m,n,h):
    visited[x][y][z] = 0
    queue_x = deque([x])
    queue_y = deque([y])
    queue_z = deque([z])
    dx = [1,-1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,1,-1]
    cnt = 0
    while queue_x:
        vx = queue_x.popleft()
        vy = queue_y.popleft()
        vz = queue_z.popleft()
        for i in range(6):
            nx = vx + dx[i]
            ny = vy + dy[i]
            nz = vz + dz[i]
            if 0 <= nx and 0 <= ny and nx < h and ny < n and nz < m and 0 <= nz:
                if visited[nx][ny][nz] >= visited[vx][vy][vz] + 1:
                    visited[nx][ny][nz] = visited[vx][vy][vz] + 1
                    if array[nx][ny][nz] == 0:
                        cnt = visited[nx][ny][nz]
                        queue_x.append(nx)
                        queue_y.append(ny)
                        queue_z.append(nz)
    return cnt

m,n,h = map(int,input().split())
box = [ [] for _ in range(h)]
t = []
for i in range(n*h):
    tmp = list(map(int,input().split()))
    box[i//n].append(tmp)
visited = [[[INF]*m for _ in range(n)] for _ in range(h)]
answer = INF
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                tmp = bfs(box,visited,i,j,k,m,n,h)
                answer = min(tmp,answer)
            elif box[i][j][k] == 0:
                t.append((i,j,k))
for i in t:
    if visited[i[0]][i[1]][i[2]] == INF:
        answer = -1
print(answer) 