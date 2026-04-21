from collections import deque

n = int(input())

r1, c1, r2, c2 = map(int,input().split())

def bfs(visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    move_type = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]
    while queue:
        vx, vy = queue.popleft()
        for move in move_type:
            nx = vx + move[0]
            ny = vy + move[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                queue.append((nx,ny))
                visited[nx][ny] = visited[vx][vy] + 1

INF = int(1e9)

move_cnt_list = [[INF]*n for _ in range(n)]

bfs(move_cnt_list,(r1,c1))

if move_cnt_list[r2][c2] == INF:
    print("-1")
else:
    print(move_cnt_list[r2][c2])