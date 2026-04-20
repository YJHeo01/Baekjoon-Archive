from collections import deque

board = []
dest_list = []
for i in range(5):
    tmp = list(map(int,input().split()))
    for j in range(5):
        if tmp[j] == 1:
            dest_list.append((i,j))
    board.append(tmp)

r,c = map(int,input().split())

INF = int(1e9)
move_cnt = [[INF]*5 for _ in range(5)]
def solution(graph,move_cnt,start):
    queue = deque([start])
    move_cnt[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or graph[nx][ny] == -1:
                continue
            if move_cnt[nx][ny] > move_cnt[vx][vy] + 1:
                move_cnt[nx][ny] = move_cnt[vx][vy] + 1
                queue.append((nx,ny))
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or graph[nx][ny] == -1:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if graph[nx][ny] == 7:
                    break
            if move_cnt[nx][ny] > move_cnt[vx][vy] + 1:
                move_cnt[nx][ny] = move_cnt[vx][vy] + 1
                queue.append((nx,ny))
solution(board,move_cnt,(r,c))

answer = INF
for x,y in dest_list:
    answer = min(answer,move_cnt[x][y])
if answer == INF:
    answer = -1

print(answer)
