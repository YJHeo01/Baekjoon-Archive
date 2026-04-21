import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

tg,tb,x,b = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(n)]

start = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == '*': start.append((i,j))
        
INF = int(1e9)

visited = [[INF]*m for _ in range(n)]

def bfs(graph,visited,start):
    q = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for x,y in start:
        visited[x][y] = 0
        heapq.heappush(q,(0,x,y))
    while q:
        dist, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            nd = dist + 1
            if graph[nx][ny] == '#': nd += tb
            if visited[nx][ny] > nd:
                visited[nx][ny] = nd
                heapq.heappush(q,(nd,nx,ny))
                
bfs(graph,visited,start)

not_exist = True

for i in range(n):
    for j in range(m):
        if visited[i][j] > tg:
            print(i+1,j+1)
            not_exist = False
            
if not_exist: print(-1)