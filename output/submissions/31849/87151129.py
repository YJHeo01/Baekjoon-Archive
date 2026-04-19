from collections import deque
import sys

input = sys.stdin.readline

def main():
    room = [list(map(int,input().split())) for _ in range(r)]
    distance = [[-1]*(m+1) for _ in range(n+1)]
    bfs(distance)
    answer = int(1e9)
    for x,y,p in room:
        answer = min(answer,distance[x][y]*p)
    print(answer)

def bfs(distance):
    queue = deque([])
    for _ in range(c):
        x,y = map(int,input().split())
        distance[x][y] = 0
        queue.append((x,y))
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > m: continue
            if distance[nx][ny] == -1:
                distance[nx][ny] = distance[vx][vy] + 1
                queue.append((nx,ny))

if __name__ == "__main__":
    n,m,r,c = map(int,input().split())
    main()