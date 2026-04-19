def main():
    n,k = map(int,input().split())
    dp = [0] * (n+1)
    dp[0],dp[1] = 1,1
    for i in range(2,n+1):
        dp[i] = (dp[i-1]*i) % 10007
    answer = dp[n] // (dp[n-k] * dp[k])
    print(answer)

if __name__ == "__main__":
    main()