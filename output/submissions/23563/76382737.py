import heapq

h,w = map(int,input().split())

maze = []

for _ in range(h):
    maze.append(list(input()))

start = (-1,-1)
end = (-1,-1)

for x in range(1,h-1):
    for y in range(1,w-1):
        if maze[x][y] == 'S':
            start = [x,y]
        if maze[x][y] == 'E':
            end = (x,y)

        if maze[x][y] != '#':
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
            adj = False
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if maze[nx][ny] == '#':
                    adj = True
                    break
            if adj == True:
                maze[x][y] = 'a'
        else:
            continue

INF = int(1e9)

visited = [[INF]*w for _ in range(h)]

def solution(graph,time,start):
    queue = []
    heapq.heappush(queue,[0]+start)
    time[start[0]][start[1]] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vt,vx,vy = heapq.heappop(queue)
        if vt > time[vx][vy]:
            continue
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '#':
                continue
            if graph[nx][ny] == 'a' and graph[vx][vy] == 'a':
                if time[nx][ny] > vt:
                    time[nx][ny] = vt
                    heapq.heappush(queue,(time[nx][ny],nx,ny))
            else:
                if time[nx][ny] > vt + 1:
                    time[nx][ny] = vt + 1
                    heapq.heappush(queue,(time[nx][ny],nx,ny))

solution(maze,visited,start)

answer = visited[end[0]][end[1]]

print(answer)