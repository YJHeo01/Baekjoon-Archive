import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    dp = [[0]*2 for _ in range(n+1)]
    INF = 1000000007
    dp[0][0], dp[0][1] = 1,0
    for i in range(n):
        a,b = map(int,input().split())
        if b == 0:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0] * (m-1) + dp[i][1]
        else:
            dp[i+1][0] = dp[i][0] * (m-1)
            dp[i+1][1] = (m-1) * dp[i][1] + dp[i][0]
        dp[i+1][0] %= INF
        dp[i+1][1] %= INF
    print(sum(dp[n])%INF)

if __name__ == "__main__":
    main()