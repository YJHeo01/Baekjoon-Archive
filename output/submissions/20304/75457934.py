from collections import deque

n = int(input())


INF = int(1e9)

visited = [INF] * (n+1)

m = int(input())

start = list(map(int,input().split()))
def solution(visited,start):
    queue = deque(start)
    for idx in start:
        visited[idx] = 0
    ret_value = 0
    while queue:
        vx = queue.popleft()
        ret_value = visited[vx]
        for i in range(20):
            nx = vx & ((2**20-1) - 2**i)
            if nx > n:
                continue
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
        for i in range(20):
            nx = vx | (2 ** i)
            if nx > n:
                break
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
    return ret_value

answer = solution(visited,start)

print(answer)