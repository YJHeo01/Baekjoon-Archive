from collections import deque

INF = 200001

n,k = map(int,input().split())

visited = [-1] * INF

queue = deque([n])

visited[n] = 0

while queue:
    vx = queue.popleft()
    if vx * 2 < INF  and visited[vx*2] == -1:
        visited[vx*2] = visited[vx]
        queue.appendleft(vx*2)
    for dx in [-1,1]:
        nx = vx + dx
        if nx < 0 or nx >= INF: continue
        if visited[nx] == -1:
            visited[nx] = visited[vx] + 1
            queue.append(nx)
            
print(visited[k])