r,c = map(int,input().split())

board = []

for _ in range(r):
    board.append(list(input()))

def move_horse(row,column,distance,visited):
    ret_value = distance
    if visited[ord(board[row][column])-ord('A')] == 1:
        return ret_value
    else:
        visited[ord(board[row][column])-ord('A')] = 1
        if row + 1 < r:
            ret_value = max(ret_value,move_horse(row+1,column,distance+1,visited))
        if column + 1 < c:
            ret_value = max(ret_value,move_horse(row,column+1,distance+1,visited))
        if row - 1 >= 0:
            ret_value = max(ret_value,move_horse(row-1,column,distance+1,visited))
        if column - 1 >= 0:
            ret_value = max(ret_value,move_horse(row,column-1,distance+1,visited))
        visited[ord(board[row][column])-ord('A')] = 0
        return ret_value

visited = [0] * 26

answer = move_horse(0,0,0,visited)

print(answer)