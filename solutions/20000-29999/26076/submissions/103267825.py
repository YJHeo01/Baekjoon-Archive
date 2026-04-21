from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(n)]

def check_zero():
    queue = deque([(0,0)])
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    while queue:
        x,y = queue.popleft()
        if x == n-1 and y == m-1: return False
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if visited[nx][ny] or maze[nx][ny] == 1: continue
            visited[nx][ny] = True
            queue.append((nx,ny))
    return True

def check_one(graph,visited,start):
    row_state = [False] * n
    column_state = [False] * m
    row_cnt = 1
    column_cnt = 1
    row_state[start[0]] = True
    column_state[start[1]] = True
    visited[start[0]][start[1]] = True
    queue = deque([start])
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if visited[nx][ny] or graph[nx][ny] == 0: continue
            if row_state[nx] == False:
                row_state[nx] = True
                row_cnt += 1
            if column_state[ny] == False:
                column_state[ny] = True
                column_cnt += 1
            visited[nx][ny] = True
            queue.append((nx,ny))
    if row_cnt == n or column_cnt == m: return 1
    return 2

def solution():
    if check_zero(): return 0
    ret_value = 2
    visited = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if maze[x][y] == 1 or visited[x][y]: continue
            ret_value = min(ret_value,check_one(maze,visited,(x,y)))
            if ret_value == 1: return 1
    return ret_value
    
answer = solution()

print(answer)