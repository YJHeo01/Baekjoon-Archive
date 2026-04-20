from collections import deque

INF = int(1e9)

visited = [[INF]*(500001) for _ in range(2)]

def bfs(visited,start):
    queue = deque([(start,0)])
    visited[0][start] = 0
    dx = [1,-1]
    while queue:
        vx,vt = queue.popleft()
        nt = (vt+1) % 2
        for i in range(2):
            nx = vx + dx[i]
            if nx < 0 or nx > 500000:
                continue
            if visited[nt][nx] > visited[vt][vx] + 1:
                visited[nt][nx] = visited[vt][vx] + 1
                queue.append((nx,nt))
        nx = vx * 2
        if nx > 500000:
            continue
        if visited[nt][nx] > visited[vt][vx] + 1:
            visited[nt][nx] = visited[vt][vx] + 1
            queue.append((nx,nt))

n,k = map(int,input().split())

answer = -1

bfs(visited,n)

time = 0

while True:
    k += time
    if k > 500000:
        break
    if visited[time%2][k] <= time:
        answer = time
        break
    time += 1

print(answer)