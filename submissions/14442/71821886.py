from collections import deque
import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

INF = int(1e9)

visited = [[[INF]*m for _ in range(n)]for _ in range(k+1)]

def solution(graph,visited):
    queue = deque([(0,0,k)])
    visited[k][0][0] = 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy, crash_cnt = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == '0':
                if nx == n-1 and ny == m-1:
                    return visited[crash_cnt][vx][vy] + 1
                if visited[crash_cnt][nx][ny] > visited[crash_cnt][vx][vy] + 1:
                    visited[crash_cnt][nx][ny] = visited[crash_cnt][vx][vy] + 1
                    queue.append((nx,ny,crash_cnt))
            else:
                if crash_cnt > 0 and visited[crash_cnt-1][nx][ny] > visited[crash_cnt][vx][vy] + 1:
                    visited[crash_cnt-1][nx][ny] = visited[crash_cnt][vx][vy] + 1
                    queue.append((nx,ny,crash_cnt-1))
    return -1

print(solution(matrix,visited))