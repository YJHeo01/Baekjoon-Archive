from collections import deque
import heapq

n = int(input())

town = [list(input()) for _ in range(n)]

high = [list(map(int,input().split())) for _ in range(n)]

start = (-1,-1)

for i in range(n):
    for j in range(n):
        if town[i][j] == 'P': start = (i,j)

INF = int(1e9)

max_high = [[INF]*n for _ in range(n)]
min_high = [[-1]*n for _ in range(n)]

q = []

start_x,start_y = start

max_high[start_x][start_y] = high[start_x][start_y]

heapq.heappush(q,(high[start_x][start_y],start_x,start_y))

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

while q:
    cur_high, vx, vy = heapq.heappop(q)
    if cur_high > max_high[vx][vy]: continue
    for i in range(8):
        nx,ny = vx + dx[i], vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        next_high = max(cur_high,high[nx][ny])
        if max_high[nx][ny] > next_high:
            max_high[nx][ny] = next_high
            heapq.heappush(q,(next_high,nx,ny))
            
min_high[start_x][start_y] = high[start_x][start_y]

heapq.heappush(q,(-high[start_x][start_y],start_x,start_y))

while q:
    cur_high, vx, vy = heapq.heappop(q)
    cur_high *= -1
    if cur_high < min_high[vx][vy]: continue
    for i in range(8):
        nx,ny = vx + dx[i], vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        next_high = min(cur_high,high[nx][ny])
        if min_high[nx][ny] < next_high:
            min_high[nx][ny] = next_high
            heapq.heappush(q,(-next_high,nx,ny))
            
max_value = 0
min_value = INF

for i in range(n):
    for j in range(n):
        if town[i][j] != 'K': continue
        max_value = max(max_value,max_high[i][j])
        min_value = min(min_value,min_high[i][j])
        
answer = max_value - min_value

print(answer)