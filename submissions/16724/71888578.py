import sys

input = sys.stdin.readline

n,m = map(int,input().split())

ground = []

for _ in range(n):
    ground.append(list(input()))

visited = [[False]*m for _ in range(n)]

answer = 0

def find_safe_zone(graph,visited,start):
    y, x = start
    while visited[y][x] == False:
        visited[y][x] = True
        if graph[y][x] == 'U':
            y -= 1
        elif graph[y][x] == 'D':
            y += 1
        elif graph[y][x] == 'L':
            x -= 1
        else:
            x += 1
    

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            find_safe_zone(ground,visited,(i,j))
            answer += 1

print(answer)