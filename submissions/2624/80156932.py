def main():
    t = int(input())
    k = int(input())
    dp = [[0]*(t+1) for _ in range(k+1)]
    dp[0][0] = 1
    for i in range(k):
        p,n = map(int,input().split())
        for j in range(t+1):
            if dp[i][j] == 0: continue
            dp[i+1][j] += dp[i][j]
            next_idx = j
            for _ in range(n):
                next_idx += p
                if next_idx > t: break
                dp[i+1][next_idx] += dp[i][j]
    print(dp[k][t])

if __name__ == "__main__":
    main()