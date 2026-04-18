import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

x,y = map(int,input().split())

a,b,c = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

INF = int(1e9)

dist = [[INF]*m for _ in range(n)]

x -= 1; y -= 1

dist[x][y] = 0

q = []

heapq.heappush(q,(0,x,y))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while q:
    d,x,y = heapq.heappop(q)
    if d > dist[x][y]: continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >=m: continue
        t = abs(arr[nx][ny]-arr[x][y])
        if t > c: continue
        nd = d
        if arr[nx][ny] > arr[x][y]: nd += a * t
        elif arr[nx][ny] < arr[x][y]: nd += b * t
        else: nd += 1
        if dist[nx][ny] > nd:
            dist[nx][ny] = nd
            heapq.heappush(q,(nd,nx,ny))

answer = dist[0][0]
answer_x, answer_y = 0,0

for i in range(n):
    for j in range(m):
        if arr[i][j] > arr[answer_x][answer_y]:
            answer_x = i
            answer_y = j
            answer = dist[i][j]
            
if answer >= INF: answer = -1

print(answer)