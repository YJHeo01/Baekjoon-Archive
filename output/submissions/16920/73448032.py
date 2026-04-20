from collections import deque
import sys

input = sys.stdin.readline

n,m,p = map(int,input().split())

S = [0] + list(map(int,input().split()))

board = []

player_last_get_castle = [[] for _ in range(p+1)]

player_score = [0] * (p+1)

for i in range(n):
    tmp = list(input())
    board.append(tmp)
    for j in range(m):
        if tmp[j] != '.' and tmp[j] != '#':
            player_idx = int(tmp[j])
            player_score[player_idx] += 1
            player_last_get_castle[player_idx].append([i,j])
            tmp[j] = player_idx
    

def bfs(graph,start):
    ret_value = []
    queue = deque([start+[0]])
    idx = graph[start[0]][start[1]]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy,move_cnt = queue.popleft()
        if move_cnt == S[idx]:
            return ret_value
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == '.':
                graph[nx][ny] = idx
                player_score[idx] += 1
                ret_value.append([nx,ny])
                queue.append([nx,ny,move_cnt+1])
            else:
                continue   
    return ret_value

while True:
    game_over = True
    for i in range(1,p+1):
        tmp = []
        for start in player_last_get_castle[i]:
            tmp += bfs(board,start)
        if tmp != []:
            game_over = False
        player_last_get_castle[i] = tmp
    if game_over == True:
        break

for i in range(1,p+1):
    print(player_score[i],end=" ")