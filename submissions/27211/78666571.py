from collections import deque
import sys

input = sys.stdin.readline

def main():
    planet = get_planet(n)
    answer = 0
    visited = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if planet[x][y] == 1 or visited[x][y] == True: continue
            visited[x][y] = True
            bfs(planet,visited,(x,y))
            answer += 1
    print(answer)

def get_planet(n):
    planet = []
    for _ in range(n): planet.append(list(map(int,input().split())))
    return planet

def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = (vx + dx[i]) % n
            ny = (vy + dy[i]) % m
            if visited[nx][ny] == True or graph[nx][ny] == 1: continue
            visited[nx][ny] = True
            queue.append((nx,ny))

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()