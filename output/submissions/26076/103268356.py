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

row_set = []
column_set = []
row_cnt = []
column_cnt = []

idx = 0

def make_block(graph,visited,start):
    global row_set,column_set,row_cnt,column_cnt
    row_state = set([start[0]])
    column_state = set([start[1]])
    visited[start[0]][start[1]] = idx
    queue = deque([start])
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if visited[nx][ny] == idx or graph[nx][ny] == 0: continue
            row_state.add(nx)
            column_state.add(ny)
            visited[nx][ny] = idx
            queue.append((nx,ny))
    row_set.append(row_state)
    column_set.append(column_state)
    row_cnt.append(len(row_state))
    column_cnt.append(len(column_state))

def solution():
    global idx
    if check_zero(): return 0
    ret_value = 2
    block = [[-1]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if maze[x][y] == 0 or block[x][y] != -1: continue
            block[x][y] = idx
            make_block(maze,block,(x,y))
            idx += 1
    for x in range(n):
        for y in range(m):
            if maze[x][y] == 1 or x + y == 0 or x + y == n + m - 2: continue
            tmp = set()
            tmp_row = 1
            tmp_column = 1
            for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m or block[nx][ny] == -1: continue
                tmp.add(block[nx][ny])
            for f in tmp:
                tmp_row += row_cnt[f]
                tmp_column += column_cnt[f]
            if tmp_row < n or tmp_column < m: continue
            row = set([x])
            column = set([y])
            for f in tmp:
                row |= row_set[f]
                column |= column_set[f]
            if len(row) == n or len(column) == m: return 1
    return ret_value
    
answer = solution()

print(answer)