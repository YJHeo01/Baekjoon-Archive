import sys

input = sys.stdin.readline

def main():
    n = int(input())
    board = get_board(n)
    print(solution(board,n))

def get_board(n):
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    return board

def solution(board,n):
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = 1
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0: continue
            if x + board[x][y] < n:
                dp[x+board[x][y]][y] += dp[x][y]
            if y + board[x][y] < n:
                dp[x][y+board[x][y]] += dp[x][y]
            
    return dp[n-1][n-1]

if __name__ == "__main__":
    main()