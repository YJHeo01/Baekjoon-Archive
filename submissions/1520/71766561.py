from collections import deque
import sys

input = sys.stdin.readline

m,n = map(int,input().split())

graph = []

for _ in range(m):
    graph.append(list(map(int,input().split())))

def bfs(graph):
    ret_value = 0
    queue = deque([(0,0)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[vx][vy] > graph[nx][ny]:
                if nx == m-1 and ny == n-1:
                    ret_value += 1
                else:
                    queue.append((nx,ny))
    return ret_value

print(bfs(graph))