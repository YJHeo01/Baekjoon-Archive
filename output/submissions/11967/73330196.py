from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[[]for _ in range(n+1)]for _ in range(n+1)]

for _ in range(m):
    x,y,a,b  = map(int,input().split())
    graph[x][y].append((a,b))

light_on = [[False]*(n+1) for _ in range(n+1)]
visited = [[False]*(n+1) for _ in range(n+1)]
def solution(graph,visited,light_on):
    ret_value = 1
    queue = deque([(1,1)])
    light_on[1][1] = True
    visited[1][1] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for x,y in graph[vx][vy]:
            if visited[x][y] == True:
                continue
            light_on[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= 0 or ny <= 0 or nx > n or ny > n:
                    continue
                if visited[nx][ny] == True:
                    ret_value += 1
                    visited[x][y] = True
                    queue.append((x,y))
                    break
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > n:
                continue
            if light_on[nx][ny] == True and visited[nx][ny] == False:
                visited[nx][ny] = True
                ret_value += 1
                queue.append((nx,ny))
    return ret_value

answer = solution(graph,visited,light_on)

print(answer)