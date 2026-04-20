from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

forest = []

for _ in range(n):
    forest.append(list(map(int,input().split())))

visited = [[0]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 1

def find_smaller(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 1
    ret_value = 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[vx][vy] > graph[nx][ny] and visited[vx][vy] + 1 > visited[nx][ny]:
                visited[nx][ny] = visited[vx][vy] + 1
                ret_value = visited[nx][ny]
                queue.append((nx,ny))
    return ret_value

def find_bigger(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 1 
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > graph[vx][vy] and visited[vx][vy] + 1 > visited[nx][ny]:
                visited[nx][ny] = visited[vx][vy] + 1
                ret_value = visited[nx][ny]
                queue.append((nx,ny))
    return ret_value

for x in range(n):
    for y in range(n):
        if visited[x][y] != 0:
            continue
        biggest = True
        smallest = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if forest[nx][ny]>forest[x][y]:
                biggest = False
            else:
                smallest = False
        if biggest == True:
            answer = max(answer,find_smaller(forest,visited,(x,y)))
        elif smallest == True:
            answer = max(answer,find_bigger(forest,visited,(x,y)))

print(answer)
