from collections import deque

n = int(input())

town = []
start = (-1,-1)
house = []
for i in range(n):
    tmp = list(input())
    for j in range(n):
        if tmp[j] == '.':
            continue
        elif tmp[j] == 'K':
            house.append((i,j))
        else:
            start = (i,j)

for _ in range(n):
    town.append(list(map(int,input().split())))

def solution(graph,visited_highest,visited_lowest,start):
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    queue = deque([start])
    visited_highest[start[0]][start[1]] = graph[start[0]][start[1]]
    visited_lowest[start[0]][start[1]] = graph[start[0]][start[1]]
    while queue:
        vx,vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if (visited_highest[nx][ny] - visited_lowest[nx][ny]) > (max(visited_highest[vx][vy],graph[nx][ny])-min(visited_lowest[vx][vy],graph[nx][ny])):
                visited_highest[nx][ny] = max(visited_highest[vx][vy],graph[nx][ny])
                visited_lowest[nx][ny] = min(visited_lowest[vx][vy],graph[nx][ny])
                queue.append((nx,ny))

INF = int(1e9)

visited_highest = [[INF]*n for _ in range(n)]
visited_lowest = [[0]*n for _ in range(n)]

solution(town,visited_highest,visited_lowest,start)

highest = visited_highest[start[0]][start[1]]
lowest = visited_lowest[start[0]][start[1]]

for x,y in house:
    highest = max(highest,visited_highest[x][y])
    lowest = min(lowest,visited_lowest[x][y])

answer = highest - lowest

print(answer)