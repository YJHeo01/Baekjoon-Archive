from collections import deque

w,h = map(int,input().split())

graph = []

start = []
dest = []
for i in range(h):
    tmp = list(input())
    if start == []:
        for j in range(w):
            if tmp[j] == 'C':
                for k in range(4):
                    start.append((i,j,k))
    elif dest == []:
        for j in range(w):
            if tmp[j] == 'C':
                for k in range(4):
                    dest.append((i,j,k))
    graph.append(tmp)

INF = int(1e9)

mirror_cnt = [[[INF]*w for _ in range(h)] for _ in range(4)]

def bfs(graph,visited,start):
    queue = deque(start)
    for x,y,d in start:
        visited[d][x][y] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy, direction = queue.popleft()
        for i in range(-1,2):
            next_d = (direction+i) % 4
            nx = vx + dx[next_d]
            ny = vy + dy[next_d]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '*':
                continue
            if i == 0:
                if visited[next_d][nx][ny] > visited[direction][vx][vy]:
                    visited[next_d][nx][ny] = visited[direction][vx][vy]
                    queue.append((nx,ny,next_d))
            else:
                if visited[next_d][nx][ny] > visited[direction][vx][vy] + 1:
                    visited[next_d][nx][ny] = visited[direction][vx][vy] + 1
                    queue.append((nx,ny,next_d))

answer = INF

bfs(graph,mirror_cnt,start)

for x,y,d in dest:
    answer = min(answer, mirror_cnt[d][x][y])

print(answer)
                 