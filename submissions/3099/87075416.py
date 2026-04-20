def main():
    s = list(input())
    length = len(s)
    dp = [[INF]*26 for _ in range(length)]
    dp[0][ord(s[0])-ord('A')] = 2
    for i in range(1,length):
        for j in range(26):
            for k in range(26):
                plus = 1
                if j != k: plus += 1
                if k != ord(s[i]) - ord('A'): plus += 1
                dp[i][k] = min(dp[i][k],dp[i-1][j]+plus)
    #print(dp)
    print(min(dp[length-1]))

if __name__ == "__main__":
    INF = int(1e9)
    main()