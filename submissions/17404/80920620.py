import sys

input = sys.stdin.readline

def main():
    INF = int(1e9)
    n = int(input())
    cost = []
    for _ in range(n):
        cost.append(list(map(int,input().split())))
    answer = INF
    for i in range(3):
        dp = [[INF]*3 for _ in range(n)]
        dp[0][i] = cost[0][i]
        for j in range(1,n):
            dp[j][0] = min(dp[j-1][1],dp[j-1][2]) + cost[j][0]
            dp[j][1] = min(dp[j-1][0],dp[j-1][2]) + cost[j][1]
            dp[j][2] = min(dp[j-1][0],dp[j-1][1]) + cost[j][2]
        for k in range(3):
            if i == k: continue
            answer = min(answer,dp[n-1][k])
    print(answer)

if __name__ == "__main__":
    main()