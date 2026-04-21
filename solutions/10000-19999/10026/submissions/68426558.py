from collections import deque

n = int(input())

def bfs(array,visited,start,color):
    queue_x = deque([start[0]])
    queue_y = deque([start[1]])
    visited[start[0]][start[1]] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue_x:
        vx = queue_x.popleft()
        vy = queue_y.popleft()

        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]

            if nx >= n or ny >= n or nx <0 or ny<0:
                continue
            if visited[nx][ny] == 0:
                if array[nx][ny] == color:
                    visited[nx][ny] = 1
                    queue_x.append(nx)
                    queue_y.append(ny)

    
array = []
visited = [[0]*n for _ in range(n)]
for i in range(n):
    tmp = list(input())
    array.append(tmp)

cnt = 0
cnt_ = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(array,visited,(i,j),array[i][j])
            cnt += 1
visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if array[i][j] == 'R':
            array[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(array,visited,(i,j),array[i][j])
            cnt_ += 1
print(cnt, end = ' ')
print(cnt_)