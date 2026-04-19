import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())

forest = []

for _ in range(n):
    forest.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]

def dfs(graph,dp,start):
    x,y = start
    if dp[x][y] != 0:
        return dp[x][y]
    ret_value = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] > graph[x][y]:
            ret_value = max(ret_value,dfs(graph,dp,(nx,ny)))
    ret_value += 1
    dp[x][y] = ret_value
    return ret_value

answer = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            answer = max(answer,dfs(forest,dp,(i,j)))

print(answer)