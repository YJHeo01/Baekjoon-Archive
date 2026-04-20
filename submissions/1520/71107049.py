from collections import deque
import sys

input = sys.stdin.readline

m,n = map(int,input().split())

ground = []

for _ in range(m):
    ground.append(list(map(int,input().split())))

def solution(graph,start):
    ret_value = 0
    q = deque([start])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while q:
        vx,vy = q.popleft()
        if vx == (m-1) and vy == (n-1):
            ret_value += 1
            continue
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] < graph[vx][vy]:
                q.append((nx,ny))
    return ret_value

print(solution(ground,(0,0)))