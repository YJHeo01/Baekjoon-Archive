from collections import deque
import sys,heapq

input = sys.stdin.readline

h,w = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(h)]

q = []

for i in range(h):
    for j in range(w):
        if maze[i][j] <= 0: continue
        heapq.heappush(q,(-maze[i][j],i,j))

array = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if maze[i][j] == -1: array[i][j] = -1

answer = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while q:
    l,x,y = heapq.heappop(q)
    l *= -1
    if array[x][y] >= l: continue
    array[x][y] = l
    queue = deque([(x,y)])
    answer += 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
            if maze[nx][ny] == -1 or array[vx][vy] - 1 < maze[nx][ny] or array[nx][ny] >= array[vx][vy] - 1: continue
            array[nx][ny] = array[vx][vy] - 1
            if array[nx][ny] > maze[nx][ny]:
                print(-1)
                exit(0)
            if array[nx][ny] != 1: queue.append((nx,ny))
                
for i in range(h):
    for j in range(w):
        if array[i][j] != maze[i][j]: answer = -1
        
print(answer)