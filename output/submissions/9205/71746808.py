import sys

input = sys.stdin.readline

t = int(input())

def dfs(graph,visited,start,dest):
    visited[start] = True
    if start == dest:
        return 1
    ret_value = 0
    for i in range(dest+1):
        if visited[i] == True:
            continue
        if abs(graph[start][0]-graph[i][0]) + abs(graph[start][1]-graph[i][1]) <= 1000:
            ret_value += dfs(graph,visited,i,dest)
    return ret_value

for _ in range(t):
    n = int(input())
    point = [[0]*2 for _ in range(n+2)]
    point[0][0],point[0][1] = map(int,input().split())
    for i in range(1,n+1):
        a,b = map(int,input().split())
        point[i][0] = a
        point[i][1] = b
    point[n+1][0], point[n+1][1] = map(int,input().split())
    visited = [False] * (n+2)
    if dfs(point,visited,0,n+1) == 1:
        print("happy")
    else:
        print("sad")