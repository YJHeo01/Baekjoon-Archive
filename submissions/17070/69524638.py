from collections import deque

n = int(input())


def bfs(graph,start):
    ret_v = 0
    queue = deque([start])
    dx = [[0,1],[1,1],[0,1,1]]
    dy = [[1,1],[0,1],[1,1,0]]
    while queue:
        vx, vy, d = queue.popleft()
        l = (d // 2) + 2
        for i in range(l):
            nx = vx + dx[d][i]
            ny = vy + dy[d][i]
            if nx == (n-1) and ny == (n-1):
                ret_v += 1
                continue
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if i == 1:
                if graph[nx][ny] == 1 or graph[nx][ny-1] == 1 or graph[nx-1][ny] == 1:
                    continue
                queue.append((nx,ny,2))
            else:
                if graph[nx][ny] == 1:
                    continue
                if dx[d][i] == 1:
                    queue.append((nx,ny,1))
                else:
                    queue.append((nx,ny,0))
    return ret_v

home = []

for _ in range(n):
    tmp = list(map(int,input().split()))
    home.append(tmp)


answer = bfs(home,(0,1,0))


print(answer)