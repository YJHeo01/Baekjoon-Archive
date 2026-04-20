m,n = map(int,input().split()) # m : 세로, n: 가로

answer = 0
def dfs(graph,start): #깊이 우선 탐색
    global answer
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx, ny = start[0] + dx[i], start[1] + dy[i] #x가 세로, y가 가로
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if graph[start[0]][start[1]] > graph[nx][ny]:
            if nx != (m-1) or ny != (n-1):
                dfs(graph,(nx,ny))
            else:
                answer += 1
            
graph = [] # 지도
for _ in range(m):
    graph.append(list(map(int,input().split())))

dfs(graph,(0,0))

print(answer)