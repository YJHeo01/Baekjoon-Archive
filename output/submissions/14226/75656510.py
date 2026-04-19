from collections import deque

s = int(input())

INF = int(1e9)

visited = [INF] * (s+1)

def solution(visited):
    queue = deque([1])
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        nx = vx - 1
        if nx >= 0 and visited[nx] > visited[vx] + 1:
            visited[nx] = visited[vx] + 1
            queue.append(nx)
        for i in range(2,1000):
            nx = vx * i
            if nx > s:
                break
            if visited[nx] > visited[vx] + i:
                visited[nx] = visited[vx] + i
                queue.append(nx)

solution(visited)

answer = visited[s]

print(answer)