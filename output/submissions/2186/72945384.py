import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))

word = list(input().rstrip())
answer = 0
word_length = len(word)

def dfs(point,length):
    if length == word_length:
        return 1
    ret_value = 0
    vx,vy = point
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx,ny = vx,vy
        for _ in range(k):
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if graph[nx][ny] == word[length]:
                ret_value += dfs((nx,ny),length+1)
    return ret_value

for i in range(n):
    for j in range(m):
        if graph[i][j] == word[0]:
            answer += dfs((i,j),1)

print(answer)