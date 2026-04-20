from collections import deque

block = [[[False]*8 for _ in range(8)]for _ in range(8)]

for i in range(8):
    tmp = list(input())
    for column in range(8):
        if tmp[column] == '.':
            continue
        for time in range(8-i):
            row = i + time
            block[time][row][column] = True


def bfs(block):
    start = 7,0,0
    dx = [-1,-1,-1,0,0,0,1,1,1]
    dy = [-1,0,1,-1,0,1,-1,0,1]
    queue = deque([start])
    while queue:
        vx,vy,move_cnt = queue.popleft()
        if move_cnt >= 7:
            return 1
        for i in range(9):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= 8 or ny >= 8 or block[move_cnt+1][nx][ny] == True or block[move_cnt][nx][ny] == True:
                continue
            queue.append((nx,ny,move_cnt+1))    
    return 0

print(bfs(block))