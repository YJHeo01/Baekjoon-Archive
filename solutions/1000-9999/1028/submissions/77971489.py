import sys

input = sys.stdin.readline

def main():
    board = get_board()
    dp_A = get_dp_A(board)
    dp_B = get_dp_B(board)
    answer = solution(dp_A,dp_B)
    print(answer)

def get_board():
    board = []
    for _ in range(r):
        tmp = list(input())
        for i in range(c):
            tmp[i] = int(tmp[i])
        board.append(tmp)
    return board

def get_dp_A(board):
    dp = [[-1]*c for _ in range(r)]
    for i in range(r):
        dp[i][0] = board[i][0] - 1
    for i in range(c):
        dp[0][i] = board[0][i] - 1
    for x in range(1,r):
        for y in range(1,c):
            if board[x][y] == 0:
                continue
            dp[x][y] = dp[x-1][y-1] + 1
    return dp

def get_dp_B(board):
    dp = [[-1]*c for _ in range(r)]
    for i in range(r):
        dp[i][c-1] = board[i][c-1] - 1
    for i in range(c):
        dp[0][i] = board[0][i] - 1
    for x in range(1,r):
        for y in range(c-2,-1,-1):
            if board[x][y] == 0:
                continue
            dp[x][y] = dp[x-1][y+1] + 1
    return dp

def solution(dp_A,dp_B):
    ret_value = 0
    for x in range(r):
        for y in range(c):
            max_size = min(dp_A[x][y],dp_B[x][y])
            for size in range(max_size,ret_value-1,-1):
                x1 = x - size; y1 = y - size
                if dp_B[x1][y1] < size:
                    continue
                x2 = x1 ; y2 = y + size
                if dp_A[x2][y2] < size:
                    continue
                ret_value = size + 1
                break
    return ret_value

if __name__ == "__main__":
    r,c = map(int,input().split())
    main()