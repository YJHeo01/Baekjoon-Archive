from collections import deque

n = int(input())

ground = []

for _ in range(n):
    ground.append(list(input()))

start = (-1,-1,-1)
end = (-1,-1,-1)

for i in range(n):
    for j in range(n):
        if ground[i][j] == 'B' and start == (-1,-1,-1):
            if j == n - 1:
                start = (i+1,j,1)
            elif ground[i][j+1] == 'B':
                start = (i,j+1,0)
            else:
                start = (i+1,j,1)
        elif ground[i][j] == 'E' and end == (-1,-1,-1):
            if j == n - 1:
                end = (i+1,j,1)
            elif ground[i][j+1] == 'E':
                end = (i,j+1,0)
            else:
                end = (i+1,j,1)

INF = int(1e9)

def get_next_state(state):
    if state == 1:
        return 0
    else:
        return 1
def check_can_turn(graph,position):
    vx,vy = position
    dx_dy = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(8):
        nx = vx + dx_dy[i][0]
        ny = vy + dx_dy[i][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == '1':
            return False
    return True
visited = [[[INF]*2 for _ in range(n)]for _ in range(n)]

def check_can_move_state0(graph,position):
    x,y = position
    dy = [1,-1]
    for i in range(2):
        ny = y + dy[i]
        if ny < 0 or ny >= n or graph[x][ny] == '1':
            return False
    return True

def check_can_move_state1(graph,position):
    x,y = position
    dx = [1,-1]
    for i in range(2):
        nx = x + dx[i]
        if nx < 0 or nx >= n or graph[nx][y] == '1':
            return False
    return True

def solution(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]][start[2]] = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while queue:
        vx,vy,state = queue.popleft()
        if check_can_turn(graph,(vx,vy)) == True:
            next_state = get_next_state(state)
            if visited[vx][vy][next_state] > visited[vx][vy][state] + 1:
                visited[vx][vy][next_state] = visited[vx][vy][state] + 1
                queue.append((vx,vy,next_state))
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == '1':
                continue
            if state == 0:
                can_move = check_can_move_state0(graph,(nx,ny))
            else:
                can_move = check_can_move_state1(graph,(nx,ny))
            if can_move == True and visited[nx][ny][state] > visited[vx][vy][state] + 1:
                visited[nx][ny][state] = visited[vx][vy][state] + 1
                queue.append((nx,ny,state)) 

solution(ground,visited,start)

answer = visited[end[0]][end[1]][end[2]]

if answer >= INF:
    answer = 0

print(answer)