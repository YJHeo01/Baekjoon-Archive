from collections import deque

n,m = map(int,input().split())

a1 = list(map(int,input().split()))

a2 = list(map(int,input().split()))

b1 = list(map(int,input().split()))

b2 = list(map(int,input().split()))

INF = int(1e9)

def search_shortest_line(start,dest,avoid_line):
    queue = deque([start])
    visited = [[INF]*(m+1) for _ in range(n+1)]
    visited[start[0]][start[1]] = 0
    avoid_x = [avoid_line[0][0],avoid_line[1][0]]
    avoid_y = [avoid_line[0][1],avoid_line[1][1]]
    avoid_x.sort()
    avoid_y.sort()
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx > n or ny > m:
                continue
            if nx < avoid_x[0] or nx > avoid_x[1] or ny < avoid_y[0] or ny > avoid_y[1]:
                if visited[nx][ny] > visited[vx][vy] + 1:
                    if nx == dest[0] and ny == dest[1]:
                        return visited[vx][vy] + 1 + avoid_x[1] - avoid_x[0] + avoid_y[1] - avoid_y[0]
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
    return INF

answer = min(search_shortest_line(a1,a2,(b1,b2)),search_shortest_line(b1,b2,(a1,a2)))

if (a2[0]-a1[0]+1) / (a2[1]-a1[1]+1) == (b2[0]-b1[0]+1) / (b2[1]-b1[1]+1):
    answer = abs(a2[0]-a1[0]) + abs(a2[1]-a1[1]) + abs(b2[1]-b1[1]) + abs(b2[0]-b1[0])
if answer >= INF:
    answer = "IMPOSSIBLE"

print(answer)