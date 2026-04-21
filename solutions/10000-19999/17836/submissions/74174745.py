from collections import deque

INF = 10001

n,m,t = map(int,input().split())

castle = []

for _ in range(n):
    castle.append(list(map(int,input().split())))

def solution(graph,time):
    queue = deque([(0,0,0)])
    time[0][0][0] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy,gram = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or time[gram][nx][ny] <= time[gram][vx][vy] + 1:
                continue
            if graph[nx][ny] == 2:
                time[1][nx][ny] = time[0][vx][vy] + 1
                queue.append((nx,ny,1))
            elif gram >= graph[nx][ny] :
                time[gram][nx][ny] = time[gram][vx][vy] + 1
                queue.append((nx,ny,gram))
            else:
                continue
    
time = [[[INF]*m for _ in range(n)]for _ in range(2)]

solution(castle,time)

answer = min(time[0][n-1][m-1],time[1][n-1][m-1])

if answer > t:
    answer = 'Fail'

print(answer)