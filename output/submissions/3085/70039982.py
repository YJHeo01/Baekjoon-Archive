answer = 0
n = int(input())
board = []

def search_candy_height_length(point):
    x,y = point
    height_length = 0
    for i in range(x,n):
        if board[i][y] == board[x][y]:
            height_length += 1
        else:
            break
    for i in range(x-1,-1,-1):
        if board[i][y] == board[x][y]:
            height_length += 1
        else:
            break
    return height_length

def search_candy_width_length(point):
    x,y = point
    width_length = 0
    for i in range(y,n):
        if board[x][i] == board[x][y]:
            width_length += 1
        else:
            break
    for i in range(y-1,-1,-1):
        if board[x][i] == board[x][y]:
            width_length += 1
        else:
            break
    return width_length
    
def Bomboni(point1,point2):
    ret_v = 0
    global board
    board[point1[0]][point1[1]], board[point2[0]][point2[1]] = board[point2[0]][point2[1]], board[point1[0]][point1[1]]
    ret_v = max(search_candy_width_length(point1),search_candy_height_length(point1),search_candy_width_length(point2),search_candy_height_length(point2))
    board[point1[0]][point1[1]], board[point2[0]][point2[1]] = board[point2[0]][point2[1]], board[point1[0]][point1[1]]
    return ret_v

for _ in range(n):
    board.append(list(input()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

answer = 0
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx, ny = i+dx[k],j+dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            answer = max(answer,Bomboni((i,j),(nx,ny)))

print(answer)