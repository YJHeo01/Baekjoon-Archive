n,m = map(int,input().split())

chess_board = [['F']*(m+1) for _ in range(n+1)]

queen_information = list(map(int,input().split()))
queen_list = []
knight_information = list(map(int,input().split()))
knight_list = []
pawn_information = list(map(int,input().split()))

answer = n*m

def set_chess_board(graph,unit_name,unit_information):
    unit_list = []
    for i in range(1,unit_information[0]*2+1,2):
        graph[unit_information[i]][unit_information[i+1]] = unit_name
        unit_list.append((unit_information[i],unit_information[i+1]))
    return unit_list

if queen_information[0] != 0:
    answer -= queen_information[0]
    queen_list = set_chess_board(chess_board,'Q',queen_information)

if knight_information[0] != 0:
    answer -= knight_information[0]
    knight_list = set_chess_board(chess_board,'K',knight_information)

if pawn_information[0] != 0:
    answer -= pawn_information[0]
    set_chess_board(chess_board,'P',pawn_information)

def check_knight(graph,position):
    ret_value = 0
    move_type = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for move in move_type:
        nx,ny = position[0] + move[0], position[1] + move[1]
        if nx <= 0 or ny <= 0 or nx > n or ny > m:
            continue
        if graph[nx][ny] == 'F':
            graph[nx][ny] = 'T'
            ret_value += 1
    return ret_value

def check_queen(graph,position):
    ret_value = 0
    move_type = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for move in move_type:
        nx, ny = position[0]+move[0], position[1]+move[1]
        while True:
            if nx <= 0 or ny <= 0 or nx > n or ny > m:
                break
            if graph[nx][ny] == 'F':
                graph[nx][ny] = 'T'
                ret_value += 1
            else:
                if graph[nx][ny] != 'T':
                    break
            nx += move[0]
            ny += move[1]
            
    return ret_value

for knight in knight_list:
    answer -= check_knight(chess_board,knight)

for queen in queen_list:
    answer -= check_queen(chess_board,queen)

print(answer)