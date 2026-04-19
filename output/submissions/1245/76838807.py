from collections import deque

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

def check_mountain_top(graph,visited,start):
    queue = deque([start])
    init_h = graph[start[0]][start[1]]
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    ret_value = True
    while queue:
        vx,vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] > graph[vx][vy]:
                if graph[nx][ny] > init_h:
                    ret_value = False
            else:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return ret_value

visited = [[False]*m for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            continue
        if visited[i][j] == False:
            if check_mountain_top(graph,visited,(i,j)) == True:
                answer += 1


print(answer)