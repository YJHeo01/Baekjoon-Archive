import sys

input = sys.stdin.readline

n = int(input())

forest = []

for _ in range(n):
    forest.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 0

def dfs(graph,start,visit_cnt):
    ret_value = visit_cnt
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    vx,vy = start
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] > graph[vx][vy]:
            ret_value = max(ret_value,dfs(graph,(nx,ny),visit_cnt+1))
    return ret_value

for x in range(n):
    for y in range(n):
        start_searching = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if forest[x][y] >= forest[nx][ny]:
                start_searching = False
                break
        if start_searching == True:
            answer = max(answer,dfs(forest,(x,y),1))

print(answer)