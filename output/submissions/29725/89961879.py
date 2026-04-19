board = [list(input()) for _ in range(8)]

answer = 0

for i in range(8):
    for j in range(8):
        if board[i][j] == 'P': answer += 1
        elif board[i][j]in ['N','B']:answer += 3
        elif board[i][j] == 'R': answer += 5
        elif board[i][j] == 'Q': answer += 9
        elif board[i][j] == 'p': answer -= 1
        elif board[i][j]in ['n','b']:answer -= 3
        elif board[i][j] == 'r': answer -= 5
        elif board[i][j] == 'q': answer -= 9
print(answer)