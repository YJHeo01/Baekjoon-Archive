from collections import deque
def bfs(array,visited,x,y,n):
    visited[x][y] = 1
    queue_x = deque([x])
    queue_y = deque([y])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 1
    while queue_x:
        vx = queue_x.popleft()
        vy = queue_y.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]

            if 0 <= nx and 0 <= ny and nx < n and ny < n:
                if visited[nx][ny] == 0 and array[nx][ny] == '1':
                    visited[nx][ny] = 1
                    queue_x.append(nx)
                    queue_y.append(ny)
                    cnt += 1
    return cnt

n = int(input())

array = []
cnt = []
count = 0
for i in range(n):
    tmp = list(input())
    array.append(tmp)

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if array[i][j] == '1' and visited[i][j] == 0:
            tmp = bfs(array, visited, i,j,n)
            cnt.append(tmp)
            count+=1            
cnt.sort()
print(count)
for i in range(count):
    print(cnt[i])