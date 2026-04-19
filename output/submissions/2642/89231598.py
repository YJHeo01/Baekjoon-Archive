from collections import deque

array = [list(map(int,input().split())) for _ in range(6)]

answer = 0

dx = [0,2,0,-2]
dy = [2,0,-2,0]

for vx in range(6):
    for vy in range(6):
        if array[vx][vy] == 1:
            for i in range(4):
                nx = vx + dx[i]
                ny = vy + dy[i]
                if nx < 0 or ny < 0 or nx >= 6 or ny >= 6: continue
                if array[nx][ny] == 0: continue
                if answer == 0:
                    answer = array[nx][ny]
                else:
                    answer = -1
     
if answer <= 0:
    print(0)
    exit(0)
    
cnt = 0

visited = [[False]*6 for _ in range(6)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for vx in range(6):
    for vy in range(6):
        if visited[vx][vy] or array[vx][vy] == 0: continue
        cnt += 1
        queue = deque([(vx,vy)])
        visited[vx][vy] = True
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= 6 or ny >= 6: continue
                if visited[nx][ny] == False and array[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

if cnt != 1:
    print(0)
    exit(0)
    
min_x, max_x, min_y, max_y = 6,-1,6,-1

for x in range(6):
    for y in range(6):
        if array[x][y] == 0: continue
        min_x = min(min_x,x)
        min_y = min(min_y,y)
        max_x = max(max_x,x)
        max_y = max(max_y,y)

x_size = max_x - min_x
y_size = max_y - min_y

if x_size * y_size == 6 and x_size + y_size == 5:
    print(answer)
else:
    print(0)