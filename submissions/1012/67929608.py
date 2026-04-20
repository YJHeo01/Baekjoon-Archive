from collections import deque

def bfs(start_x,start_y,array):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue_x = deque([start_x])
    queue_y = deque([start_y])
    visited[start_y][start_x] = True
    while(queue_x):
        x = queue_x.popleft()
        y = queue_y.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <m and nx > -1 and ny > -1 and ny < n and not visited[ny][nx] and array[ny][nx] == 1:
                queue_x.append(nx)
                queue_y.append(ny)
                visited[ny][nx] = True






t = int(input())
cnt = 0
index = []
for i in range(t):
    global m,n,k
    m, n, k = input().split()
    m = int(m)
    n = int(n)
    k = int(k)
    array = [[0]*m for _ in range(n)]
    for j in range(k):
        x, y = input().split()
        x,y = int(x),int(y)
        array[y][x] = 1
        index.append((x,y))
    global visited
    visited = [[False]*m for _ in range(n)]

    for i in index:
        if not visited[i[1]][i[0]]:
            bfs(i[0],i[1],array)
            cnt += 1

    print(cnt)
    cnt = 0
    index = []