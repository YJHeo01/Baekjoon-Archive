#https://github.com/YJHeo01
from collections import deque

n,m = map(int,input().split())

campus = []
doyeon = (-1,-1)
for i in range(n):
    campus.append(list(input()))
    for j in range(m):
        if campus[i][j] == 'I':
            doyeon = (i,j)
            break

def find_people(graph,visited,start):
    answer = 0
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'X' or visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            queue.append((nx,ny))
            if graph[nx][ny] == 'P':
                answer += 1
    return answer

visited = [[False]*m for _ in range(n)]

answer = find_people(campus,visited,doyeon)

if answer == 0:
    answer = 'TT'

print(answer)