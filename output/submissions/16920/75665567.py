import sys

from collections import deque

input = sys.stdin.readline

INF = int(1e9)

n,m,p = map(int,input().split())

player_move_limit = [0] + list(map(int,input().split()))

new_area = [[]for _ in range(p+1)]


answer = [0] * (p+1)

board = []

for _ in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(m):
        if board[i][j].isdigit() == True:
            idx = int(board[i][j])
            board[i][j] = idx
            new_area[idx].append((i,j))
            answer[idx] += 1

def get_new_area(board,visited,start):
    queue = deque(start)
    player_idx = board[start[0][0]][start[0][1]]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = []
    for point in start:
        x,y = point
        visited[x][y] = 0
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
                answer[player_idx] += 1
                if visited[nx][ny] < player_move_limit[player_idx]:
                    queue.append((nx,ny))
                else:
                    ret_value.append((nx,ny))
    return ret_value


while True:
    game_over = True
    for i in range(1,p+1):
        if new_area[i] == []:
            continue
        game_over = False
        visited = [[INF]*m for _ in range(n)]
        new_area[i] = get_new_area(board,visited,new_area[i])
    if game_over == True:
        break

for i in range(1,p+1):
    print(answer[i],end=" ")