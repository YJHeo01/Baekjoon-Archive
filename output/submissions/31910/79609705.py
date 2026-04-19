def main():
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = array[0][0]
    for i in range(1,n):
        dp[0][i] += dp[0][i-1] * 2
        dp[0][i] += array[0][i]
    for i in range(1,n):
        dp[i][0] += dp[i-1][0] * 2
        dp[i][0] += array[i][0]
        for j in range(1,n):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) * 2
            dp[i][j] += array[i][j]
    print(dp[n-1][n-1])
            
if __name__  == "__main__":
    n = int(input())
    main()