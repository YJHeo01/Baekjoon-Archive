from collections import deque

INF = 200000
second = [INF] * 200000

n,k= map(int,input().split())

def bfs(visited,start):
    queue = deque([start])
    visited[start] = 0
    dx = [-1,0,1]
    while queue:
        v = queue.popleft()
        for i in dx:
            if i == 0:
                nx = v*2
            else: nx = v + i

            if nx < 0 or nx >= INF:
                continue
            if visited[v] + 1 < visited[nx]:
                queue.append(nx)
                visited[nx] = visited[v] + 1

bfs(second,n)

print(second[k])