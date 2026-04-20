from collections import deque
import sys

input = sys.stdin.readline

n,m,k,t = map(int,input().split())

visited = [[[False]*(n+1) for _ in range(n+1)]for _ in range(2)]

start = []

for _ in range(m):
    start.append(list(map(int,input().split())) + [0])

def solution(visited,start):
    queue = deque(start)
    dx = [2,2,1,1,-1,-1,-2,-2]
    dy = [1,-1,2,-2,2,-2,1,-1]
    for x,y,z in start:
        visited[z%2][x][y] = True
    while queue:
        vx, vy, time = queue.popleft()
        if time == t:
            continue
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > n:
                continue
            if visited[(time+1)%2][nx][ny] == True:
                continue
            visited[(time+1)%2][nx][ny] = True
            queue.append((nx,ny,time+1))

solution(visited,start)
yes = False

for _ in range(k):
    a,b = map(int,input().split())
    if visited[t%2][a][b] == True:
        yes = True

if n < 3:
    yes = False
    
if yes == True:
    print("YES")
else:
    print("NO")