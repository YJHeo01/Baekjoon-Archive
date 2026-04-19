from collections import deque

n,t,g = map(int,input().split())

INF = int(1e9)

visited = [INF] * 100000
def solution(visited,start,limit):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        if visited[vx] == limit:
            break
        if vx < 99999:
            nx = vx + 1
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
        if vx < 50000:
            if vx == 0:
                continue
            nx = vx * 2
            for i in range(4,-1,-1):
                num = 10 ** i
                if nx >= num:
                    nx -= num
                    if visited[nx] > visited[vx] + 1:
                        visited[nx] = visited[vx] + 1
                        queue.append(nx)
                    break

solution(visited,n,t)

answer = visited[g]

if answer >= INF:
    answer = 'ANG'

print(answer)