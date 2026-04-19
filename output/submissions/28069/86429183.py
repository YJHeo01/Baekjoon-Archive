from collections import deque

n,k = map(int,input().split())
visited = [k+1] * (n+1)

def bfs(visited):
    queue = deque([0])
    visited[0] = 0
    while queue:
        vx = queue.popleft()
        for dx in [1,vx//2]:
            nx = vx + dx
            if nx > n or visited[nx] <= visited[vx] + 1: continue
            visited[nx] = visited[vx] + 1
            queue.append(nx)
bfs(visited)

if visited[n] > k:
    print("water")
else:
    print("minigimbob")