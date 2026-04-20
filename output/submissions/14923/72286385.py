from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

start = list(map(int,input().split()))
destination = list(map(int,input().split()))

start[0] -= 1; start[1] -= 1; destination[0] -= 1; destination[1] -= 1

matrix = []

for _ in range(n):
    matrix.append(list(map(int,input().split())))
INF = int(1e9)

distance_list = [[INF]*m for _ in range(n)]

def find_block(graph,visited,start):
    block_list = []
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                if graph[nx][ny] == 0:
                    queue.append((nx,ny))
                else:
                    block_list.append((nx,ny))
    return block_list

can_crash_block = find_block(matrix,distance_list,start)

def crash_block(graph,visited,start):
    queue = deque(start)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1 and graph[nx][ny] == 0:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    return visited[destination[0]][destination[1]]

answer = crash_block(matrix,distance_list,can_crash_block)

if answer >= INF:
    answer = -1

print(answer)