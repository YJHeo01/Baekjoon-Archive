from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

visited = [[False]*(n+1) for _ in range(n+1)]

switch_on = [[False]*(n+1) for _ in range(n+1)]

graph = [[[]for _ in range(n+1)]for _ in range(n+1)]

for _ in range(m):
    x,y,a,b = map(int,input().split())
    graph[x][y].append((a,b))

def solution(graph,visited,switch_on):
    ret_value = 0
    queue = deque([(1,1)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        if visited[vx][vy] == True:
            continue
        visited[vx][vy] = True
        ret_value += 1
        for x,y in graph[vx][vy]:
            if visited[x][y] == True:
                continue
            switch_on[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= 0 or ny <= 0 or nx > n or ny > n:
                    continue
                if visited[nx][ny] == True:
                    queue.append((x,y))
                    break
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > n or visited[nx][ny] == True:
                continue
            if switch_on[nx][ny] == True:
                queue.append((nx,ny))
    return ret_value

answer = solution(graph,visited,switch_on)

print(answer)
