n,m = map(int,input().split())

def check_mountain_peak(graph,visited,start):
    ret_value = True
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    x,y = start
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m :
            continue
        if graph[nx][ny] > graph[x][y]:
            ret_value = False
            break
        elif graph[nx][ny] == graph[x][y]:
            if visited[nx][ny] == True:
                continue
            ret_value = ret_value and check_mountain_peak(graph,visited,(nx,ny))
        else:
            continue
    if ret_value == False:
        visited[x][y] = False
    return ret_value

mountain = []

for _ in range(n):
    mountain.append(list(map(int,input().split())))


answer = 0
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j] == True:
            continue
        if check_mountain_peak(mountain,visited,(i,j)) == True:
            answer += 1

print(answer)