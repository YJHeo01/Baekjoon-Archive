from collections import deque

n = int(input())

bridge = list(map(int,input().split()))

start = int(input()) - 1

visited = [False] * n

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    while queue:
        vx = queue.popleft()
        dx = [graph[vx],-graph[vx]]
        for i in range(2):
            nx = vx + dx[i]
            if nx < 0 or nx >= n:
                continue
            if visited[nx] == False:
                visited[nx] = True
                queue.append(nx)

bfs(bridge,visited,start)

answer = 0

for i in range(n):
    if visited[i] == True:
        answer += 1

print(answer)