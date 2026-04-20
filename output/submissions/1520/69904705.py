import sys

input = sys.stdin.readline

from collections import deque

m,n = map(int,input().split()) # m : 세로, n: 가로

def search(graph,start): #탐색
    ret_v = 0
    queue = deque([start])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx, ny = vx + dx[i], vy + dy[i] #x가 세로, y가 가로
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[vx][vy] > graph[nx][ny]:
                if nx != (m-1) or ny != (n-1):
                    queue.append((nx,ny))
                else:
                    ret_v += 1
    return ret_v
            
graph = [] # 지도
for _ in range(m):
    graph.append(list(map(int,input().split())))

answer = search(graph,(0,0))

print(answer)