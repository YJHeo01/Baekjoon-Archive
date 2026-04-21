def main():
    n = int(input())
    array = list(map(int,input().split()))
    dp = [1] * n; answer = 1
    for i in range(1,n):
        for j in range(i):
            if array[j] >= array[i]:continue
            if dp[i] >= dp[j] + 1: continue
            dp[i] = dp[j] + 1
            answer = max(answer,dp[i])    
    print(answer)

if __name__ == "__main__":
    main()