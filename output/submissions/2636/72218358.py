from collections import deque

cheese = []

r,c = map(int,input().split())

for _ in range(r):
    cheese.append(list(map(int,input().split())))

def melt_cheese(graph,visited,start):
    queue = deque(start)
    next_melt_cheese = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                if graph[nx][ny] == 1:
                    next_melt_cheese.append((nx,ny))
                else:
                    queue.append((nx,ny))
    return next_melt_cheese

start = [(0,0),(0,c-1),(r-1,0),(r-1,c-1)]

visited = [[False]*c for _ in range(r)]
first_answer = 0
second_answer = 0

while True:
    next_start = melt_cheese(cheese,visited,start)
    if next_start == []:
        second_answer = len(start)
        break
    first_answer += 1
    start = next_start

print(first_answer)
print(second_answer)
