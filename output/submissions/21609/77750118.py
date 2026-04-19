from collections import deque

RAINBOW = 0
EMPTY = -2

def main():
    board = get_board(); answer = 0
    while True:
        visited = [[False]*n for _ in range(n)]
        target_point = (-1,-1)
        target_block_cnt = 1; target_rainbow_block_cnt = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] <= 0 or visited[i][j] == True:
                    continue
                tmp_block_cnt, tmp_rainbow_block_cnt = get_block_cnt(board,visited,(i,j))
                if tmp_block_cnt > target_block_cnt or (tmp_block_cnt == target_block_cnt and tmp_rainbow_block_cnt >= target_rainbow_block_cnt):
                    target_block_cnt = tmp_block_cnt; target_rainbow_block_cnt = tmp_rainbow_block_cnt; target_point = (i,j)
        if finish_game(target_block_cnt) == True:
            break
        answer += (target_block_cnt ** 2)
        remove_block(board,target_point)
        gravity(board)
        board = turn_counterclockwise(board)
        gravity(board)
    print(answer)

def get_board():
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    return board

def get_block_cnt(graph,visited,start):
    queue = deque([start])
    target_color = graph[start[0]][start[1]]
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1]; dy = [1,0,-1,0]
    tmp_block_cnt, tmp_rainbow_block_cnt = 1,0
    rainbow_block = []
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_board(nx,ny) == True or visited[nx][ny] == True:
                continue
            if graph[nx][ny] == RAINBOW:
                rainbow_block.append((nx,ny))
                tmp_rainbow_block_cnt += 1
            else:
                if graph[nx][ny] != target_color:
                    continue
            visited[nx][ny] = True
            tmp_block_cnt += 1
            queue.append((nx,ny))
    visited = init_rainbow_block(visited,rainbow_block)
    return tmp_block_cnt, tmp_rainbow_block_cnt

def exit_board(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return True
    return False

def init_rainbow_block(visited,block):
    for x,y in block:
        visited[x][y] = False
    return visited
    
def remove_block(graph,start):
    queue = deque([start])
    target_idx = graph[start[0]][start[1]]
    dx = [0,1,0,-1]; dy = [1,0,-1,0]
    graph[start[0]][start[1]] = EMPTY
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_board(nx,ny) == True:
                continue
            if graph[nx][ny] == target_idx or graph[nx][ny] == RAINBOW:
                graph[nx][ny] = EMPTY
                queue.append((nx,ny))

def gravity(graph):
    for i in range(n-2,-1,-1):
        for j in range(n):
            if graph[i][j] < 0:
                continue
            move_block(graph,(i,j))

def move_block(graph,start):
    x,y = start
    while True:
        x += 1
        if x >= n or graph[x][y] != EMPTY:
            break
        graph[x][y],graph[x-1][y] = graph[x-1][y],graph[x][y]

def turn_counterclockwise(board):
    new_board = [[EMPTY]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            new_board[get_nx(y)][get_ny(x)] = board[x][y]
    return new_board

def get_nx(y):
    return n - 1 - y

def get_ny(x):
    return x

def finish_game(block_cnt):
    if block_cnt <= 1:
        return True
    return False

if __name__ == "__main__":
    n, m = map(int,input().split())
    main()