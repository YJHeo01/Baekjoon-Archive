from collections import deque

n, m = map(int,input().split())

def bfs(graph,visited,start):
    ret_val = 1
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                ret_val += 1
    return ret_val


picture = []

visited = [[0] * m for _ in range(n)]

for _ in range(n):
    picture.append(list(map(int,input().split())))

answer = 0
pic_cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and picture[i][j] == 1:
            tmp = bfs(picture,visited,(i,j))
            answer = max(tmp,answer)
            pic_cnt += 1
print(pic_cnt)
print(answer)