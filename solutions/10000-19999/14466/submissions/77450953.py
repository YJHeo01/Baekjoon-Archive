from collections import deque
import sys

input = sys.stdin.readline

n,k,r = map(int,input().split())
road = [[[]for _ in range(n+1)]for _ in range(n+1)]
cow = []
for _ in range(r):
    r1,c1,r2,c2 = map(int,input().split())
    road[r1][c1].append([r2,c2])
    road[r2][c2].append([r1,c1])

for _ in range(k):
    cow.append(list(map(int,input().split())))

def bfs(road,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > n or [nx,ny] in road[vx][vy]:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append([nx,ny])

answer = 0

for start_cow_idx in range(k-1):
    visited = [[False]*(n+1) for _ in range(n+1)]
    start = cow[start_cow_idx]
    bfs(road,visited,start)
    for end_cow in range(start_cow_idx+1,k):
        x,y = cow[end_cow]
        if visited[x][y] == False:
            answer += 1

print(answer)