from collections import deque

array = [list(map(int,input().split())) for _ in range(6)]

answer = 0

cnt = 0

visited = [[{(-1,0):0,(1,0):0,(0,-1):0,(0,1):0} for _ in range(6)] for _ in range(6)]

dx_dy_list = [(-1,0),(1,0),(0,-1),(0,1)]
for vx in range(6):
    for vy in range(6):
        if array[vx][vy] != 1: continue
        cnt += 1
        queue = deque([(vx,vy)])
        while queue:
            x,y = queue.popleft()
            for dx_dy in dx_dy_list:
                dx,dy = dx_dy
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= 6 or ny >= 6: continue
                if visited[nx][ny] == {(-1,0):0,(1,0):0,(0,-1):0,(0,1):0} and array[nx][ny] > 1:
                    for tmp in visited[x][y]:
                        if tmp == dx_dy:
                            visited[nx][ny][tmp] = visited[x][y][tmp] + 1
                        else:
                            visited[nx][ny][tmp] = visited[x][y][tmp]

                    queue.append((nx,ny))

if cnt != 1:
    print(0)
    exit(0)
    
min_x, max_x, min_y, max_y = 6,-1,6,-1

for x in range(6):
    for y in range(6):
        if array[x][y] == 0: continue
        for tmp in visited[x][y]:
            if visited[x][y][tmp] == 2:
                if answer != 0: answer = -1
                else: answer = array[x][y]
        min_x = min(min_x,x)
        min_y = min(min_y,y)
        max_x = max(max_x,x)
        max_y = max(max_y,y)

x_size = max_x - min_x
y_size = max_y - min_y

if x_size * y_size != 6 or x_size + y_size != 5 or answer == -1:
    answer = 0
    
print(answer)
