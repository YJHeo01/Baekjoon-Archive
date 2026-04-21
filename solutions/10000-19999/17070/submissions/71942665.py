from collections import deque

n = int(input())

house = []

for i in range(n):
    house.append(list(map(int,input().split())))

def bfs(graph,start):
    ret_value = 0
    queue = deque([start])
    while queue:
        vx, vy, d = queue.popleft()
        for i in range(-1,2):
            next_d = d + i
            if next_d < -1 or next_d > 1:
                continue
            if next_d == -1:
                nx = vx
                ny = vy + 1
            elif next_d == 0:
                nx = vx + 1
                ny = vy + 1
            else:
                nx = vx + 1
                ny = vy
            if nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                if next_d == 0 and (graph[nx-1][ny] == 1 or graph[nx][ny-1] == 1):
                    continue
                if nx == n-1 and ny == n-1:
                    ret_value += 1
                else:
                    queue.append((nx,ny,next_d))
    return ret_value

print(bfs(house,(0,1,-1)))