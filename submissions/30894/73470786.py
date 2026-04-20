from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())


start_x, start_y, end_x, end_y = map(int,input().split())

house = [[0]]

ghost_list = []
ghost_zone = [[[False]*(m+1) for _ in range(n+1)] for _ in range(4)]

for i in range(1,n+1):
    tmp = list(input())
    for j in range(m):
        if tmp[j] != '.':
            for k in range(4):
                ghost_zone[k][i][j+1] = True
            if tmp[j] != '#':
                ghost_list.append((i,j+1,int(tmp[j])))
    house.append([0]+tmp)



def check_ghost_zone(graph,visited,start):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    vx,vy,d = start
    for time in range(4):
        nd = (d + time) % 4
        nx,ny = vx,vy
        while True:
            nx += dx[nd]
            ny += dy[nd]
            if nx <=0 or ny <= 0 or nx > n or ny > m or graph[nx][ny] != '.':
                break
            visited[time][nx][ny] = True

INF = int(1e9)
visited = [[[INF]*(m+1) for _ in range(n+1)]for _ in range(4)]

for ghost in ghost_list:
    check_ghost_zone(house,ghost_zone,ghost)

def solution(graph,visited,start):
    queue = deque([start])
    visited[0][start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy,vt = queue.popleft()
        for k in range(1,5):
            nt = vt + k
            for i in range(4):
                nx = vx + dx[i]
                ny = vy + dy[i]
                if nx <= 0 or ny <= 0 or nx > n or ny > m or graph[nt%4][nx][ny] == True:
                    continue
                if visited[nt%4][nx][ny] > visited[vt%4][vx][vy] + k:
                    visited[nt%4][nx][ny] = visited[vt%4][vx][vy] + k
                    queue.append((nx,ny,nt))
            if graph[nt%4][vx][vy] == True or visited[nt%4][vx][vy] <= visited[vt%4][vx][vy] + k:
                break
            visited[nt%4][vx][vy] = visited[vt%4][vx][vy] + k 
    ret_value = INF
    for i in range(4):
        ret_value = min(visited[i][end_x][end_y],ret_value)
    return ret_value
    

answer = solution(ghost_zone,visited,(start_x,start_y,0))

if answer >= INF:
    print("GG")
else:
    print(answer)