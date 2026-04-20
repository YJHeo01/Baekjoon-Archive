from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)

k = int(input())

w,h = map(int,input().split())

visited = [[[INF]*w for _ in range(h)]for _ in range(k+1)]

ground = []
for _ in range(h):
    ground.append(list(map(int,input().split())))

def move_monkey(graph,visited):
    queue = deque([(0,0,k)])
    for i in range(k,-1,-1):
        visited[i][0][0] = 0
    monkey_dx = [0,1,0,-1]
    monkey_dy = [1,0,-1,0]
    horse_dx = [1,1,2,2,-1,-1,-2,-2]
    horse_dy = [2,-2,1,-1,2,-2,1,-1]
    while queue:
        vx, vy, horse_move_cnt = queue.popleft()
        for i in range(4):
            nx = vx + monkey_dx[i]
            ny = vy + monkey_dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == 1:
                continue
            if visited[horse_move_cnt][nx][ny] > visited[horse_move_cnt][vx][vy] + 1:
                visited[horse_move_cnt][nx][ny] = visited[horse_move_cnt][vx][vy] + 1
                queue.append((nx,ny,horse_move_cnt))
        if horse_move_cnt > 0:
            for i in range(8):
                nx = vx + horse_dx[i]
                ny = vy + horse_dy[i]
                if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == 1:
                    continue
                if visited[horse_move_cnt-1][nx][ny] > visited[horse_move_cnt][vx][vy] + 1:
                    visited[horse_move_cnt-1][nx][ny] = visited[horse_move_cnt][vx][vy] + 1
                    queue.append((nx,ny,horse_move_cnt-1))
    ret_value = INF
    for i in range(k,-1,-1):
        ret_value = min(ret_value,visited[i][h-1][w-1])
    if ret_value == INF:
        ret_value = -1
    return ret_value


print(move_monkey(ground,visited))