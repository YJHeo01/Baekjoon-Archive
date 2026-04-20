from collections import deque

def main():
    global n, MID, length
    n,m = map(int,input().split())
    length = n ** 2; MID = (n-1) // 2
    board = get_board()
    line_up = get_line_up()
    answer = 0
    for _ in range(m):
        magic = list(map(int,input().split()))
        answer += blizard(board,line_up,magic)
    print(answer)
    
def get_board():
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    board[MID][MID] = -1
    return board

def get_line_up():
    line_up = []
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    x,y = MID, MID
    move_length = 1
    while True:
        for i in range(4):
            for _ in range(move_length):
                line_up.append((x,y))
                x += dx[i]; y += dy[i]
                if y < 0:
                    return line_up
            if i % 2 != 0:
                move_length += 1
    return line_up

def blizard(graph,line_up,magic):
    destroy(graph,magic)
    move_ball(graph,line_up)
    ret_value = 0
    while True:
        tmp = search_bang(graph,line_up)
        if tmp == 0:
            break
        ret_value += tmp
        move_ball(graph,line_up)
    graph = change_board(graph,line_up)
    return ret_value
    
def destroy(graph,magic):
    x, y = MID, MID
    d,s = magic
    dx = [0,-1,1,0,0]
    dy = [0,0,0,-1,1]
    ret_value = 0
    for _ in range(s):
        x += dx[d]
        y += dy[d]
        ret_value += graph[x][y]
        graph[x][y] = 0
    return ret_value

def move_ball(graph,line_up):
    blank_idx, target_idx = 0,0
    while True:
        if blank_idx >= length:
            return
        x,y = line_up[blank_idx]
        blank_idx += 1
        if graph[x][y] != 0:
            target_idx = blank_idx + 1
            continue
        while True:
            if target_idx >= length:
                return
            nx,ny = line_up[target_idx]
            if graph[nx][ny] == 0:
                target_idx += 1
                continue
            graph[x][y] = graph[nx][ny]
            graph[nx][ny] = 0; target_idx += 1
            break

def search_bang(graph,line_up):
    ret_value = 0; combo_cnt = 0
    left = 0; right = 1
    while True:
        if right >= length:
            if combo_cnt >= 4:
                ret_value += bang(graph,line_up,left,right)
            break
        vx,vy = line_up[left]
        nx,ny = line_up[right]
        if graph[vx][vy] == graph[nx][ny]:
            combo_cnt += 1; right += 1
            continue
        if combo_cnt >= 4:
            ret_value += bang(graph,line_up,left,right)
        left = right; right += 1; combo_cnt = 1
    return ret_value
            
def bang(graph,line_up,start,end):
    x,y = line_up[start]
    ret_value = (end - start) * graph[x][y]
    for i in range(start,end):
        x,y = line_up[i]
        graph[x][y] = 0
    return ret_value

def change_board(graph,line_up):
    ball_list = get_ball_list(graph,line_up)
    idx = 0
    while True:
        if idx >= length:
            break
        value = 0
        if ball_list != deque([]):
            value = ball_list.popleft()
        x,y = line_up[idx]
        graph[x][y] = value
        idx += 1
    return graph

def get_ball_list(graph,line_up):
    ret_value = deque([-1])
    combo_cnt = 1; left = 1; right = 2
    while True:
        vx,vy = line_up[left]
        if graph[vx][vy] == 0:
            break
        if right >= length:
            ret_value.append(combo_cnt)
            ret_value.append(graph[vx][vy])
            break  
        nx,ny = line_up[right]
        if graph[vx][vy] == graph[nx][ny]:
            combo_cnt += 1; right += 1
        else:
            ret_value.append(combo_cnt)
            ret_value.append(graph[vx][vy])
            left = right; right += 1; combo_cnt = 1
    return ret_value

if __name__ == "__main__":
    main()