from collections import deque

INF = int(1e9)

n,m,p = map(int,input().split())

player_move_limit = [0] + list(map(int,input().split()))

new_area = [[]for _ in range(p+1)]

board = []

for _ in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(m):
        if board[i][j].isdigit() == True:
            idx = int(board[i][j])
            board[i][j] = idx
            new_area[idx].append((i,j))

def get_new_area(board,visited,start):
    queue = deque([])
    player_idx = int(board[start[0][0]][start[0][1]])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = []
    for point in start:
        x,y = point
        if visited[x][y] != 0:
            visited[x][y] = 0
            queue.append((x,y))
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == '.' and visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                board[nx][ny] = player_idx
                ret_value.append((nx,ny))
                if visited[nx][ny] < player_move_limit[player_idx]:
                    queue.append((nx,ny))
    return ret_value


while True:
    game_over = True
    for i in range(1,p+1):
        if new_area[i] == []:
            continue
        game_over = False
        visited = [[INF]*m for _ in range(n)]
        new_area[i] = get_new_area(board,visited,new_area[i])
        for x,y in new_area[i]:
            board[x][y] = i
    if game_over == True:
        break

answer = [0] * (p+1)

for i in range(n):
    for j in range(m):
        if type(board[i][j]) == str:
            continue
        answer[board[i][j]] += 1

for i in range(1,p+1):
    print(answer[i],end=" ")