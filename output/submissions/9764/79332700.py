def main():
    dp = [0] * 2001
    dp[0] = 1
    for i in range(1,2001):
        for j in range(2000,i-1,-1):
            dp[j] += dp[j-i]
            dp[j] %= 100999
    t = int(input())
    for _ in range(t):
        n = int(input())
        answer = dp[n]
        print(answer)

if __name__ == "__main__":
    main()