import sys

input = sys.stdin.readline

from collections import deque

n,m,k,t = map(int,input().split())

visited = [[-1]*(n+1) for _ in range(n+1)]

start = []

for _ in range(m):
    start.append(list(map(int,input().split())))

def bfs(visited,start):
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 0
    dx = [1,1,2,2,-1,-1,-2,-2]
    dy = [2,-2,1,-1,2,-2,1,-1]
    while queue:
        vx,vy = queue.popleft()
        if visited[vx][vy] >= t:
            continue
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > n:
                continue
            if visited[nx][ny] < visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

yes = False

bfs(visited,start)

for _ in range(k):
    a,b = map(int,input().split())
    if visited[a][b] == t:
        yes = True

if yes == True:
    print("YES")
else:
    print("NO") 