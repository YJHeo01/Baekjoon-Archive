from collections import deque
n,m= map(int,input().split())
array = [] 
visited = [ [False] * m for _ in range(n)]
for i in range(n):
    array.append(list(input()))
def bfs(x,y,text):
    queue_x = deque([x])
    queue_y = deque([y])
    
    visited[y][x] = True
    move = [1,-1]
    if text == '-':
        while(queue_x):
            x_ = queue_x.popleft()
            for i in range(2):
                nx = x_ + move[i]
                if nx < m and nx >-1 and not visited[y][nx]:
                    if array[y][nx] == '-':
                        queue_x.append(nx)
                        visited[y][nx] = True
    else:
        while(queue_y):
            y_ = queue_y.popleft()
            for i in range(2):
                ny = y_ + move[i]
                if  ny < n and ny >-1 and not visited[ny][x]:
                    if array[ny][x] != '-' :
                        queue_y.append(ny)
                        visited[ny][x] = True
    

cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(j,i,array[i][j])
            cnt += 1

print(cnt)