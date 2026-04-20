from collections import deque
def bfs(end_x,end_y,visited,array):
    queue_x = deque([0])
    queue_y = deque([0])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[0][0] = 1
    while(queue_x):
        v_x = queue_x.popleft()
        v_y = queue_y.popleft()
        for i in range(4):
            nx = v_x + dx[i]
            ny = v_y + dy[i]
            if ny <= end_y and nx <= end_x and ny >-1 and nx > -1:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[v_y][v_x] + 1
                    if ny == end_y and nx == end_x:
                        return visited[ny][nx]
                    if array[ny][nx] == 1:
                        queue_x.append(nx)
                        queue_y.append(ny)



n, m = map(int,input().split())

mirro = []

visited = [[0] * m for _ in range(n)]

for i in range(n):
    a = list(map(int,input()))
    mirro.append(a)

print(bfs(m-1,n-1,visited,mirro))