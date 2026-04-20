def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer = 1
    dp = [1] * n
    for i in range(1,n):
        if array[i] >= array[i-1]:
            dp[i] = dp[i-1] + 1
            answer = max(answer,dp[i])
    dp = [1] * n
    for i in range(1,n):
        if array[i] <= array[i-1]:
            dp[i] = dp[i-1] + 1
            answer = max(answer,dp[i])
    print(answer)

if __name__ == "__main__":
    main()