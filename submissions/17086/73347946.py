from collections import deque

n,m = map(int,input().split())


shark = []
for i in range(n):
    tmp = list(map(int,input().split()))    
    for j in range(m):
        if tmp[j] == 1:
            shark.append((i,j))

INF = int(1e9)

visited = [[INF]*m for _ in range(n)]

def solution(visited,start):
    ret_value = 0
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 0
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,-1,1,-1,1]
    while queue:
        vx,vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                ret_value = max(ret_value,visited[nx][ny])
                queue.append((nx,ny))
    return ret_value

print(solution(visited,shark))