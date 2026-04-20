import sys

input = sys.stdin.readline

def main():
    cnt = [0] * 1001
    cnt[1] = 10
    INF = 1234567
    dp = [[[0]*5 for _ in range(6)] for _ in range(1001)]
    position = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1)]
    dx_dy = [(0,1),(0,-1),(1,0),(-1,0)]
    for x,y in position:
        dp[1][x][y] = 1
    for k in range(2,1001):
        for x,y in position:
            for dx,dy in dx_dy:
                dp[k][x][y] += dp[k-1][x+dx][y+dy]  
            dp[k][x][y] %= INF
            cnt[k] += dp[k][x][y]
        cnt[k] %= INF
    t = int(input())
    for _ in range(t):
        print(cnt[int(input())])

if __name__ == "__main__":
    main()