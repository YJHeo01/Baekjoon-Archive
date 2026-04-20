from collections import deque

n, m = map(int,input().split())
def measure_power(graph,visited,start):
    ret_value = 1
    country = graph[start[0]][start[1]]
    visited[start[0]][start[1]] = 1
    queue = deque([start])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >=n:
                continue
            if graph[nx][ny] == country and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                ret_value += 1
                queue.append((nx,ny))
    return ret_value ** 2

war = []

for _ in range(m):
    war.append(list(input()))
my_team_power = 0
enermy_power = 0
visited = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            tmp = measure_power(war,visited,(i,j))
            if war[i][j] == 'W':
                my_team_power += tmp
            else:
                enermy_power += tmp

print(my_team_power,enermy_power)