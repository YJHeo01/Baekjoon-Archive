from collections import deque
import sys

input = sys.stdin.readline

def main():
    start = list(map(int,input().split()))
    graph = [list(map(int,input().split())) for _ in range(n)]
    distance = [[-1]*m for _ in range(n)]
    bfs(graph,distance,start)
    max_dist = 0
    for tmp in distance:
        max_dist = max(max_dist,max(tmp))
    profit = [0] * (max_dist+1)
    for i in range(n):
        for j in range(m):
            dist = distance[i][j]
            if dist == -1: continue
            profit[dist] += graph[i][j]
    tmp = 0
    answer = 0
    for i in range(max_dist+1):
        tmp += profit[i]
        answer = max(answer,tmp-i*c)
    print(answer)
def bfs(graph,distance,start):
    x,y = start
    x -= 1; y -= 1
    distance[x][y] = 0
    queue = deque([(x,y)])
    while queue:
        vx,vy = queue.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx = vx + dx
            ny = vy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if graph[nx][ny] != -1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[vx][vy] + 1
                queue.append((nx,ny))

if __name__ == "__main__":
    n,m,c = map(int,input().split())
    main()