def main():
    n,k = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(n+1)]
    dp = [[[0,0,0] for _ in range(k+1)] for _ in range(n)]
    dp[0][0][0] = sum(array[0])
    dp[0][1][1] = array[0][1]
    dp[0][1][2] = array[0][0]
    for i in range(1,n):
        for close_cnt in range(k):
            dp[i][close_cnt][0] = max(dp[i-1][close_cnt]) + sum(array[i])
            dp[i][close_cnt+1][1] = max(dp[i-1][close_cnt][1],dp[i-1][close_cnt][0]) + array[i][1]
            dp[i][close_cnt+1][2] = max(dp[i-1][close_cnt][2],dp[i-1][close_cnt][0]) + array[i][0]
        dp[i][k][0] = max(max(dp[i-1][k])+sum(array[i]),dp[i][k][0])
    print(max(dp[n-1][k]))

if __name__ == "__main__":
    main()