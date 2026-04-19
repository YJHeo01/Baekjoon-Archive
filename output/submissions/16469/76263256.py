from collections import deque

r,c = map(int,input().split())

maze = []

for _ in range(r):
    maze.append(list(input()))

nuksal = list(map(int,input().split()))
swings = list(map(int,input().split()))
changmo = list(map(int,input().split()))

nuksal[0] -= 1; nuksal[1] -= 1; swings[0] -= 1; swings[1] -= 1; changmo[0] -= 1; changmo[1] -= 1

INF = int(1e9)

nuksal_visited = [[INF]*c for _ in range(r)]
swings_visited = [[INF]*c for _ in range(r)]
changmo_visited = [[INF]*c for _ in range(r)]

def solution(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] == '1':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

solution(maze,nuksal_visited,nuksal)
solution(maze,swings_visited,swings)
solution(maze,changmo_visited,changmo)

not_exist = True
min_time = INF
min_time_point_cnt = 1

for i in range(r):
    for j in range(c):
        tmp_time = max(nuksal_visited[i][j],changmo_visited[i][j],swings_visited[i][j])
        if tmp_time == INF:
            continue
        not_exist = False
        if min_time > tmp_time:
            min_time = tmp_time
            min_time_point_cnt = 1
        elif min_time == tmp_time:
            min_time_point_cnt += 1
        else:
            continue

if not_exist == True:
    print(-1)
else:
    print(min_time)
    print(min_time_point_cnt)