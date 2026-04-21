import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

forest = []

for _ in range(n):
    forest.append(list(map(int,input().split())))

visited_bigger = [[0]*n for _ in range(n)]
visited_smaller = [[0]*n for _ in range(n)]
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

def solution(graph,visited_bigger,visited_smaller,start):
    ret_value = 1
    ret_value_reverse = 1
    vx,vy = start
    visited_smaller[vx][vy], visited_bigger[vx][vy] = 1,1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] > graph[vx][vy]:
            visited_bigger[nx][ny] = 2
            ret_value = max(ret_value,search_bigger(graph,visited_bigger,(nx,ny)))
        else:
            visited_smaller[nx][ny] = 2
            ret_value_reverse = max(ret_value_reverse,search_smaller(graph,visited_smaller,(nx,ny)))
    return ret_value + ret_value_reverse - 1

answer = 0

for i in range(n):
    for j in range(n):
        if visited_bigger[i][j] == 0:
            answer = max(answer,solution(forest,visited_bigger,visited_smaller,(i,j)))

print(answer)