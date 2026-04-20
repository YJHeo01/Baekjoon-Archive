import sys
from collections import deque
input = sys.stdin.readline

global l,r,c

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]][start[2]] = 0
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    while queue:
        vx,vy,vz = queue.popleft()
        for i in range(6):
            nx = vx + dx[i]
            ny = vy + dy[i]
            nz = vz + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= l or ny >= r or nz >= c:
                continue
            if graph[nx][ny][nz] != '#':
                if graph[nx][ny][nz] == 'E':
                    return visited[vx][vy][vz] + 1
                if visited[nx][ny][nz] > visited[vx][vy][vz] + 1:
                    visited[nx][ny][nz] = visited[vx][vy][vz] + 1
                    queue.append((nx,ny,nz))
    return -1

while 1:
    start = (-1,-1,-1)
    l,r,c = map(int,input().split())
    if l == 0 and r == 0 and c == 0:
        break
    building = []
    for i in range(l):
        rows = []
        for j in range(r):
            row = list(input())
            rows.append(row)
            if start != (-1,-1,-1):
                continue
            for k in range(c):
                if row[k] == 'S':
                    start = (i,j,k)
                    break
        row = input()
        building.append(rows)
    INF = int(1e9)
    minute_list = [[[INF]*c for _ in range(r)]for _ in range(l)]
    answer = bfs(building,minute_list,start)
    if answer < 0:
        print("Trapped!")
    else:
        print("Escaped in " + str(answer) +  " minute(s).") 