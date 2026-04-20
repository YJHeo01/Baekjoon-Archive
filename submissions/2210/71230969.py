visited = [False] * 1000000

graph = []
for _ in range(5):
    graph.append(list(map(int,input().split())))

answer = 0
def dfs(point,digit,value):
    global answer
    global visited
    if digit == 6:
        if visited[value] == False:
            visited[value] = True
            answer += 1
        return
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = point[0] + dx[i]
        ny = point[1] + dy[i]
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue
        dfs((nx,ny),digit+1,value*10 + graph[nx][ny])
    return

for i in range(5):
    for j in range(5):
        dfs((i,j),1,graph[i][j])

print(answer)
