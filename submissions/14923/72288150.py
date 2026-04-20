from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

start = list(map(int,input().split())) + [1]
destination = list(map(int,input().split()))

start[0] -= 1; start[1] -= 1; destination[0] -= 1; destination[1] -= 1

matrix = []

for _ in range(n):
    matrix.append(list(map(int,input().split())))
INF = int(1e9)

distance_list = [[[INF]*m for _ in range(n)]for _ in range(2)]

def solution(graph,visited,start):
    queue = deque([start])
    visited[1][start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy, non_crash = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                if visited[non_crash][nx][ny] > visited[non_crash][vx][vy] + 1:
                    visited[non_crash][nx][ny] = visited[non_crash][vx][vy] + 1
                    queue.append((nx,ny,non_crash))
            else:
                if non_crash == 1:
                    if visited[0][nx][ny] > visited[1][vx][vy] + 1:
                        visited[0][nx][ny] = visited[1][vx][vy] + 1
                        queue.append((nx,ny,0))
    
    return min(visited[1][destination[0]][destination[1]],visited[0][destination[0]][destination[1]])

answer = solution(matrix,distance_list,start)

if answer >= INF:
    answer = -1

print(answer)