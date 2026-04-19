import sys

input = sys.stdin.readline

def main():
    cnt = [0] * 1001
    cnt[1] = 10
    INF = 1234567
    dp = [[[0]*5 for _ in range(6)] for _ in range(1001)]
    for i in range(1,4):
        for j in range(1,4):
            dp[1][i][j] = 1
    dp[1][4][1] = 1
    for k in range(2,1001):
        for vx in range(1,5):
            for vy in range(1,4):
                if vx >= 4 and vy >= 2: break
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    dp[k][vx][vy] += dp[k-1][vx+dx][vy+dy]
                dp[k][vx][vy] %= INF
                cnt[k] += dp[k][vx][vy]
        cnt[k] %= INF
    t = int(input())
    for _ in range(t):
        print(cnt[int(input())])

if __name__ == "__main__":
    main()