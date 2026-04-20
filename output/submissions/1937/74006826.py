import sys

input = sys.stdin.readline

n = int(input())

forest = []

for _ in range(n):
    forest.append(list(map(int,input().split())))

visited = [[0]*n for _ in range(n)]

def search_bigger(graph,visited,point):
    vx, vy = point
    ret_value = visited[vx][vy]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] > graph[vx][vy] and visited[vx][vy] + 1 > visited[nx][ny]:
            visited[nx][ny] = visited[vx][vy] + 1
            ret_value = max(ret_value,search_bigger(graph,visited,(nx,ny)))
    return ret_value


def search_smaller(graph,visited,point):
    vx, vy = point
    ret_value = visited[vx][vy]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] > graph[vx][vy] :
            continue
        if visited[vx][vy] + 1 > visited[nx][ny]:
            visited[nx][ny] = visited[vx][vy] + 1
            ret_value = max(ret_value,search_smaller(graph,visited,(nx,ny)))
    return ret_value

def solution(graph,visited,start):
    ret_value = 0
    ret_value_reverse = 0
    vx,vy = start
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[vx][vy] = True
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] > graph[vx][vy]:
            ret_value = max(ret_value,search_bigger(graph,visited,(nx,ny)))
        else:
            ret_value_reverse = max(ret_value_reverse,search_smaller(graph,visited,(nx,ny)))
    return ret_value + ret_value_reverse + 1

answer = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            answer = max(answer,solution(forest,visited,(i,j)))

print(answer)