from collections import deque

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
        if target_block_cnt <= 1:
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
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] == True:
                continue
            if graph[nx][ny] == 0:
                rainbow_block.append((nx,ny))
                tmp_rainbow_block_cnt += 1
            else:
                if graph[nx][ny] != target_color:
                    continue
            visited[nx][ny] = True
            tmp_block_cnt += 1
            queue.append((nx,ny))
    for x,y in rainbow_block:
        visited[x][y] = False
    return tmp_block_cnt, tmp_rainbow_block_cnt

def remove_block(graph,start):
    queue = deque([start])
    target_idx = graph[start[0]][start[1]]
    dx = [0,1,0,-1]; dy = [1,0,-1,0]
    graph[start[0]][start[1]] = -2
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == target_idx or graph[nx][ny] == 0:
                graph[nx][ny] = -2
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
        if x >= n or graph[x][y] != -2:
            break
        graph[x][y],graph[x-1][y] = graph[x-1][y],graph[x][y]

def turn_counterclockwise(board):
    new_board = [[-2]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            nx = n - 1 - y
            ny = x
            new_board[nx][ny] = board[x][y]
    return new_board

if __name__ == "__main__":
    n, m = map(int,input().split())
    main()