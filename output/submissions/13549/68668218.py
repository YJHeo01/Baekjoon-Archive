from collections import deque

INF = int(1e9)

n, k = map(int,input().split())
max_v = 2*max(n,k)
visited = [INF] * (max_v+1) 
def bfs(visited,start):
    queue = deque([start])
    visited[start] = 0
    dx = [0,1,-1]
    while queue:
        vx = queue.popleft()
        for i in dx:
            if i == 0:
                nx = vx * 2
                if nx < 0 or nx >max_v:
                    continue
                if visited[nx] > visited[vx]:
                    visited[nx] = visited[vx]
                    queue.append(nx)
            else:
                nx = vx + i
                if nx < 0 or nx > max_v:
                    continue
                if visited[nx] > visited[vx] + 1:
                    visited[nx] = visited[vx] + 1
                    queue.append(nx)

bfs(visited,n)
                
print(visited[k])