from collections import deque

array = [list(map(int,input().split())) for _ in range(6)]

answer = 0

cnt = 0

move = [[{(-1,0):0,(1,0):0,(0,-1):0,(0,1):0} for _ in range(6)] for _ in range(6)]

visited = {(-1,0):0,(1,0):0,(0,-1):0,(0,1):0}
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
                if move[nx][ny] == {(-1,0):0,(1,0):0,(0,-1):0,(0,1):0} and array[nx][ny] > 1:
                    for tmp in move[x][y]:
                        if tmp == dx_dy:
                            move[nx][ny][tmp] = move[x][y][tmp] + 1
                        else:
                            move[nx][ny][tmp] = move[x][y][tmp]

                    queue.append((nx,ny))

if cnt != 1:
    print(0)
    exit(0)

for x in range(6):
    for y in range(6):
        if array[x][y] <= 1: continue
        for tmp in move[x][y]:
            if visited[tmp] == 3:
                visited[(-tmp[0],-tmp[1])] = 1
                visited[tmp] = 0
        for tmp in move[x][y]:
            visited[tmp] = max(visited[tmp],move[x][y][tmp])
            if move[x][y][tmp] == 2:
                if answer != 0: answer = -1
                else: answer = array[x][y]

for tmp in visited:
    if visited[tmp] == 0: answer = 0

if answer == -1: answer = 0
    
print(answer)