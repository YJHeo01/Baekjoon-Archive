def main():
    k = int(input())
    dp = [1,0]
    for _ in range(k):
        cnt_a = dp[1]
        cnt_b = dp[0] + dp[1]
        dp = [cnt_a,cnt_b]
    print(*dp)

if __name__  == "__main__":
    main()