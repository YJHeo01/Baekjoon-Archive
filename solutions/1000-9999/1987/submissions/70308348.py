r,c = map(int,input().split())

board = []

for _ in range(r):
    board.append(list(input()))

def move_horse(row,column,distance,visited):
    ret_value = 0
    if row < 0 or column < 0 or row >= r or column >= c or visited[ord(board[row][column])-ord('A')] == 1:
        return distance
    else:
        visited[ord(board[row][column])-ord('A')] = 1
        ret_value = max(move_horse(row+1,column,distance+1,visited),move_horse(row,column+1,distance+1,visited),move_horse(row-1,column,distance+1,visited),move_horse(row,column-1,distance+1,visited))
        visited[ord(board[row][column])-ord('A')] = 0
        return ret_value

visited = [0] * 26

answer = move_horse(0,0,0,visited)

print(answer)