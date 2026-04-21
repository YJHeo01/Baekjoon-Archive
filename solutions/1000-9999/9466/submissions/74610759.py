import sys

input = sys.stdin.readline

t = int(input())

def dfs(graph,visited,start,point):
    visited[point] = True
    nx = graph[point]
    if nx == start:
        return 0
    if visited[nx] == True:
        visited[point] = False
        return 1
    ret_value = dfs(graph,visited,start,nx)
    if ret_value == 1:
        visited[point] = False
    return ret_value



for _ in range(t):
    n = int(input())
    array = [0] + list(map(int,input().split()))
    answer = 0
    visited = [False] * (n+1)
    for i in range(1,n+1):
        if visited[i] == False:
            answer += dfs(array,visited,i,i)
    print(answer)