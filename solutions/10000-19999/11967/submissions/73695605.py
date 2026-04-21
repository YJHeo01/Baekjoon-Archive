import sys

input = sys.stdin.readline

n,m = map(int,input().split())

visited = [[False]*(n+1) for _ in range(n+1)]

light = [[False]*(n+1) for _ in range(n+1)]

graph = [[[]for _ in range(n+1)]for _ in range(n+1)]

for _ in range(m):
    x,y,a,b = map(int,input().split())
    graph[x][y].append((a,b))

visited[0][1] = True
light[1][1] = True

answer = 0

def possible_visit(visited,start):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = start
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > n or ny > n:
            continue
        if visited[nx][ny] == True:
            return True
    return False

def switch_on(graph,light,start):
    x,y = start
    for nx,ny in graph[x][y]:
        light[nx][ny] = True
    return

while True:
    tmp = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if visited[i][j] == True:
                continue
            if light[i][j] == True:
                if possible_visit(visited,(i,j)) == True:
                    visited[i][j] = True
                    tmp += 1
                    switch_on(graph,light,(i,j))
    if tmp == 0:
        break
    answer += tmp

print(answer)