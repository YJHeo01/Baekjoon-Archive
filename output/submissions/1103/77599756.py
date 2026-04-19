import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    board = get_board()
    init_board(board)
    dp = [[INF]*m for _ in range(n)]
    dp[0][0] = 0
    answer = solution(board,dp)
    if answer == 2501:
        answer = -1
    print(answer)

def get_board():
    board = []
    for _ in range(n):
        board.append(list(input()))
    return board

def init_board(board):
    for i in range(n):
        for j in range(m):
            if board[i][j] != 'H':
                board[i][j] = int(board[i][j])

def solution(board,dp):
    answer = 0
    for i in range(2501):
        for vx in range(n):
            for vy in range(m):
                if board[vx][vy] == 'H' or dp[vx][vy] != i:
                    continue
                dx = [board[vx][vy],-board[vx][vy],0,0]
                dy = [0,0,board[vx][vy],-board[vx][vy]]
                for k in range(4):
                    nx = vx + dx[k]
                    ny = vy + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == 'H':
                        continue
                    dp[nx][ny] = i + 1
                    answer = i + 1
        if answer == i:
            answer += 1
            break
    return answer

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()