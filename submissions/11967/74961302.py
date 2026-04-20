from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())

can_visit = [[False]*(n+1) for _ in range(n+1)]
visited = [[False]*(n+1) for _ in range(n+1)]
light_on = [[False]*(n+1) for _ in range(n+1)]
switch = [[[]for _ in range(n+1)]for _ in range(n+1)]

for _ in range(m):
    x,y,a,b = map(int,input().split())
    switch[x][y].append((a,b))

def solution(graph,can_visit,visited,light_on):
    queue = deque([(1,1)])
    ret_value = 1
    can_visit[1][1] = True
    light_on[1][1] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[1][1] = True
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > n:
                continue
            can_visit[nx][ny] = True
            if light_on[nx][ny] == True and visited[nx][ny] == False:
                visited[nx][ny] = True
                ret_value += 1
                queue.append((nx,ny))
        for nx,ny in graph[vx][vy]:
            light_on[nx][ny] = True
            if can_visit[nx][ny] == True and visited[nx][ny] == False:
                visited[nx][ny] = True
                ret_value += 1
                queue.append((nx,ny))
    return ret_value

answer = solution(switch,can_visit,visited,light_on)

print(answer)