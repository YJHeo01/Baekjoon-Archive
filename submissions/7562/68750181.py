from collections import deque

INF = int(1e9)
def bfs(graph,start,l):
    queue = deque([start])
    graph[start[0]][start[1]] = 0
    dx = [1,-1,1,-1,2,-2,2,-2]
    dy = [2,2,-2,-2,1,1,-1,-1]
    while queue:
        vx, vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if graph[nx][ny] > graph[vx][vy] + 1:
                graph[nx][ny] = graph[vx][vy] + 1
                queue.append((nx,ny))
    

t = int(input())

for i in range(t):
    l = int(input())
    chess = [[INF]*l for _ in range(l)]
    a,b = map(int,input().split())
    a_,b_ = map(int,input().split())
    bfs(chess,(a,b),l)
    print(chess[a_][b_])