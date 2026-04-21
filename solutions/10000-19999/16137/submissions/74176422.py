from collections import deque

INF = 10001

n,m = map(int,input().split())

area = []

for _ in range(n):
    area.append(list(map(int,input().split())))

def solution(graph,visited):
    queue = deque([(0,0,0)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[0][0][0] = 0
    next_time = 0
    while queue:
        vx,vy,use_bird_bridge = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] != 1 and graph[vx][vy] != 1:
                continue
            if graph[nx][ny] == 1:
                if visited[use_bird_bridge][nx][ny] > visited[use_bird_bridge][vx][vy] + 1:
                    visited[use_bird_bridge][nx][ny] = visited[use_bird_bridge][vx][vy] + 1
                    queue.append((nx,ny,use_bird_bridge))
                    continue
            elif graph[nx][ny] == 0:
                if use_bird_bridge == 1:
                    continue
                next_time = ((visited[use_bird_bridge][vx][vy] // m)+1) * m
            else:
                next_time = ((visited[use_bird_bridge][vx][vy]// graph[nx][ny])+1) * graph[nx][ny]
            if visited[use_bird_bridge][nx][ny] > next_time:
                visited[use_bird_bridge][nx][ny] = next_time
                queue.append((nx,ny,use_bird_bridge))

visited = [[[INF]*n for _ in range(n)]for _ in range(2)]

solution(area,visited)

answer = min(visited[0][n-1][n-1],visited[1][n-1][n-1])

print(answer)