import sys

input = sys.stdin.readline

t = int(input())

def dfs(graph,visited,start,point):
    visited[point] = True
    nx = graph[point]
    if nx == start:
        return 1
    if visited[nx] == True:
        visited[point] = False
        return 0
    ret_value = dfs(graph,visited,start,nx)
    if ret_value == 0:
        visited[point] = False
    else:
        ret_value += 1
    return ret_value



for _ in range(t):
    n = int(input())
    array = [0] + list(map(int,input().split()))
    answer = n
    visited = [False] * (n+1)
    for i in range(1,n+1):
        if visited[i] == False:
            answer -= dfs(array,visited,i,i)
    print(answer)