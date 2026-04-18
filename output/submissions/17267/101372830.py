import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

L,R = map(int,input().split())

maze = [list(input().rstrip()) for _ in range(n)]

INF = int(1e9)

distance = [[(INF,INF) for _ in range(m)] for _ in range(n)]

q = []

for i in range(n):
    for j in range(m):
        if maze[i][j] == '2':
            distance[i][j] = (0,0)
            heapq.heappush(q,(0,0,i,j))

while q:
    l,r,x,y = heapq.heappop(q)
    if distance[x][y] != (l,r): continue
    for dx,dy in [(-1,0),(1,0)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
        if maze[nx][ny] == '1': continue
        if distance[nx][ny] > (l,r):
            distance[nx][ny] = (l,r)
            heapq.heappush(q,(l,r,nx,ny))
    if y != m-1 and R != r and maze[x][y+1] != '1':
        nx = x
        ny = y + 1
        nl,nr = l,r+1
        if distance[nx][ny] > (nl,nr):
            distance[nx][ny] = (nl,nr)
            heapq.heappush(q,(nl,nr,nx,ny))
    if y != 0 and L != l and maze[x][y-1] != '1':
        nx, ny = x, y-1
        nl, nr = l+1,r
        if distance[nx][ny] > (nl,nr):
            distance[nx][ny] = (nl,nr)
            heapq.heappush(q,(nl,nr,nx,ny))

answer = 0

for i in range(n):
    for j in range(m):
        if distance[i][j] != (INF,INF): answer += 1

print(answer)