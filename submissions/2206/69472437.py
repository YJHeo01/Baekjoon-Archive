from collections import deque

INF = int(1e9)


n, m = map(int,input().split())

def bfs(graph):
    ret_v = -1
    queue = deque([(0,0,0,1)])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vx, vy, break_block,distance = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if nx == (n-1) and ny == (m-1):
                ret_v = distance + 1
                return ret_v
            if break_block == 0:
                queue.append((nx,ny,graph[nx][ny],distance+1))
            else:
                if graph[nx][ny] == 0:
                    queue.append((nx,ny,1,distance+1))
        



                
        




graph = []

for _ in range(n):
    tmp = list(input())
    for i in range(m):
        tmp[i] = int(tmp[i])
    graph.append(tmp)

answer = bfs(graph)


print(answer)