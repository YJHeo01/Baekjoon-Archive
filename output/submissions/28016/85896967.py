import sys

input = sys.stdin.readline

def main():
    array = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    for i in range(m):
        if array[0][i] == 2:
            dp[0][i] = 1
            break
    for vx in range(n-1):
        for vy in range(m):
            if array[vx][vy] == 1: continue
            if array[vx+1][vy] == 0:
                dp[vx+1][vy] += dp[vx][vy]
            else:
                for dy in [1,-1]:
                    can_move = True
                    for dx in [0,1]:
                        if array[vx+dx][vy+dy] == 1: can_move = False
                    if can_move:
                        dp[vx+1][vy+dy] += dp[vx][vy]
    answer = 0
    for i in range(m):
        if dp[n-1][i] > dp[n-1][answer]:
            answer = i
    if dp[n-1][answer] == 0: answer = -1
    print(answer)

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()