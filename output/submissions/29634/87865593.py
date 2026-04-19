from collections import deque
n,m = map(int,input().split())
graph = [list(input())for _ in range(n)]
visited = [[False]*m for _ in range(n)]
answer = -1
for x in range(n):
    for y in range(m):
        if visited[x][y] or graph[x][y] == '*': continue
        tmp = 1
        queue = deque([(x,y)])
        visited[x][y] = True
        while queue:
            vx,vy = queue.popleft()
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = vx+dx,vy+dy
                if nx < 0 or ny < 0 or nx >= n or ny >=m: continue
                if graph[nx][ny] == '.' and visited[nx][ny] == False:
                    tmp += 1
                    visited[nx][ny] = True
                    queue.append((nx,ny))
        answer = max(answer,tmp)
print(answer)