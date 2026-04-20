import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

city = [list(input().rstrip()) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if visited[nx][ny] or graph[nx][ny] == '1': continue
            visited[nx][ny] = True
            queue.append((nx,ny))

for i in range(n):
    if city[i][0] == '0' and visited[i][0] == False:
        visited[i][0] = True
        bfs(city,visited,(i,0))
    if city[i][m-1] == '0' and visited[i][m-1] == False:
        visited[i][m-1] = True
        bfs(city,visited,(i,m-1))
        
for j in range(m):
    if city[0][j] == '0' and visited[0][j] == False:
        visited[0][j] = True
        bfs(city,visited,(0,j))
    if city[n-1][j] == '0' and visited[n-1][j] == False:
        visited[n-1][j] = True
        bfs(city,visited,(n-1,j))
        
prefix_sum = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j]
        if visited[i][j] == False: prefix_sum[i+1][j+1] += 1
        

q = int(input())

for _ in range(q):
    x1,y1,x2,y2 = map(int,input().split())
    answer = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    if answer == 0:
        print("Yes")
    else:
        print("No",answer)