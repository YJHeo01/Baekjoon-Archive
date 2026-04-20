def main():
    n = int(input())
    init_board = [list(input()) for _ in range(n)]
    player = [list(input()) for _ in range(n)]
    answer = [['.']*n for _ in range(n)]
    defeat = False
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for i in range(n):
        for j in range(n):
            if player[i][j] != 'x': continue
            if init_board[i][j] == '*':
                defeat = True
                answer[i][j] = '*'
                continue
            tmp = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
                if init_board[nx][ny] == '*': tmp += 1
            answer[i][j] = tmp
    if defeat == True:
        for i in range(n):
            for j in range(n):
                if init_board[i][j] == '*': answer[i][j] = '*'
    for i in range(n):
        for j in range(n):
            print(answer[i][j],end="")
        print()

if __name__ == "__main__":
    main()