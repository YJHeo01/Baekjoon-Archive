from collections import deque

n = int(input())


graph = []

def solution(graph):
    queue = deque([(0,1,0)])
    ret_value = 0
    dx = [0,1,1]
    dy = [1,1,0]
    while queue:
        vx,vy,d = queue.popleft()
        if vx == n-1 and vy == n-1:
            ret_value += 1
            continue
        for i in range(-1,2):
            nd = d + i
            if nd < 0 or nd > 2:
                continue
            nx = vx + dx[nd]
            ny = vy + dy[nd]
            if nx >= n or ny >= n or graph[nx][ny] == 1:
                continue
            if nd == 1 and (graph[vx][ny] == 1 or graph[nx][vy] == 1):
                continue
            queue.append((nx,ny,nd))
    return ret_value

for _ in range(n):
    graph.append(list(map(int,input().split())))

answer = solution(graph)

print(answer)