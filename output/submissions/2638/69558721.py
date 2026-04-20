from collections import deque

n,m = map(int,input().split())

def check_inside_or_outside_air(graph):
    visited = [[0]*m for _ in range(n)]
    queue = deque([(0,0)])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    graph[0][0] = 2
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if graph[nx][ny] != 1 and visited[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx,ny))
                visited[nx][ny] = 1
                
                


def check_melt_cheese(graph):
    melt_cheese = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                out_air_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if graph[nx][ny] == 2:
                        out_air_cnt += 1
                if out_air_cnt >= 2:
                    melt_cheese.append((i,j))
    if melt_cheese == []:
        return 0
    for melt in melt_cheese:
        graph[melt[0]][melt[1]] = 2
    return 1



    

paper = []

for _ in range(n):
    tmp = list(map(int,input().split()))
    paper.append(tmp)
answer = 0
check_inside_or_outside_air(paper)
while 1:
    tmp = check_melt_cheese(paper)
    if tmp == 0:
        break
    answer += 1
print(answer)