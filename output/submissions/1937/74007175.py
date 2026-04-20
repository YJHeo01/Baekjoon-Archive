import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

forest = []

for _ in range(n):
    forest.append(list(map(int,input().split())))

visited = [[0]*n for _ in range(n)]

def solution(graph,visited,start):
    vx,vy = start
    ret_value = visited[vx][vy]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] > graph[vx][vy]:
            visited[nx][ny] = visited[vx][vy] + 1
            ret_value = max(ret_value,solution(graph,visited,(nx,ny)))
    return ret_value

answer = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            answer = max(answer,solution(forest,visited,(i,j)))

print(answer)