from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

rf,cf,rh,ch = map(int,input().split())
rf -= 1; cf -= 1; rh -= 1; ch -= 1

def bfs(graph,distance,visited):
    queue = deque([(rf,cf,0)])
    distance[rf][cf][0] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy,ignore = queue.popleft()
        for i in range(4):
            nx = vx + graph[vx][vy] * dx[i]
            ny = vy + graph[vx][vy] * dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if distance[nx][ny][ignore] == -1:
                distance[nx][ny][ignore] = distance[vx][vy][ignore] + 1
                queue.append((nx,ny,ignore))
        if ignore == 1: continue
        for i in range(4):
            if visited[vx][vy][i]: continue
            visited[vx][vy][i] = True
            nx,ny = vx,vy
            while True:
                nx += dx[i]; ny += dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny][i] or distance[nx][ny][1] != -1: break
                visited[nx][ny][i], visited[nx][ny][(i+2)%4] = True, True
                distance[nx][ny][1] = distance[vx][vy][0] + 1
                queue.append((nx,ny,1))

graph = [list(map(int,input().split())) for _ in range(n)]    
distance = [[[-1]*2 for _ in range(m)] for _ in range(n)]
visited = [[[False]*4 for _ in range(m)] for _ in range(n)]

bfs(graph,distance,visited)

if min(distance[rh][ch]) == -1:
    print(max(distance[rh][ch]))
else:
    print(min(distance[rh][ch]))