from collections import deque

r,c = map(int,input().split())

start = (-1,-1)
board = []
for i in range(r):
    tmp = list(input())
    board.append(tmp)
    if start != (-1,-1):
        continue
    for j in range(c):
        if tmp[j] == 'M':
            start = (i,j)
visited = [[False]*(c) for _ in range(r)]

def search_blank(graph,visited,start):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    x,y = start[0],start[1]
    queue = deque([])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if graph[nx][ny] != '.':
            visited[nx][ny] = True
            queue.append((nx,ny))
    while queue:
        vx,vy = queue.popleft()
        possible_move = [False] * 4
        if graph[vx][vy] in ('|','+','2','3'):#top
            possible_move[0] = True
        if graph[vx][vy] in ('|','+','1','4'):#bottom
            possible_move[1] = True
        if graph[vx][vy] in ('-','+','3','4'):#left
            possible_move[2] = True
        if graph[vx][vy] in ('-','+','1','2'):#right
            possible_move[3] = True
        for i in range(4):
            if possible_move[i] == False:
                continue
            nx = vx + dx[i]
            ny = vy + dy[i]
            if visited[nx][ny] == True:
                continue
            if graph[nx][ny] == '.':
                return (nx,ny)
            visited[nx][ny] = True
            queue.append((nx,ny))

blank = search_blank(board,visited,start)

for i in range(2):
    print(blank[i]+1,end=" ")

def check_pipe(graph,point,i):
    x,y = point
    if graph[x][y] == '+':
        return True
    if i == 0:
        if graph[x][y] in ('|','1','4'):
            return True
    elif i == 1:
        if graph[x][y] in ('|','3','2'):
            return True
    elif i == 2:
        if graph[x][y] in ('-','1','2'):
            return True
    else:
        if graph[x][y] in ('-','3','4'):
            return True    
    return False

def search_pipeline(graph,blank):
    not_void = [False] * 4
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    vx, vy = blank
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        not_void[i] = check_pipe(graph,(nx,ny),i)
    if not_void[0] == True and not_void[1] == True:
        if not_void[2] == True:
            return '+'
        else:
            return '|'
    elif not_void[2] == True and not_void[3] == True:
        if not_void[0] == True:
            return '+'
        else:
            return '-'
    else:
        if not_void[0] == True:
            if not_void[2] == True:
                return '3'
            else:
                return '2'
        if not_void[2] == True:
            return '4'
        return '1'

print(search_pipeline(board,blank))
