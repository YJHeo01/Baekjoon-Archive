def main():
    n = int(input())
    array = list(map(int,input().split()))
    dp = [0] * n
    answer = 0
    for i in range(n):
        dp[i] = array[i]
        answer = max(answer,array[i])
        for j in range(i):
            if array[j] < array[i] and dp[j] + array[i] > dp[i]:
                dp[i] = dp[j] + array[i]
                answer = max(answer,dp[i])
    print(answer)

if __name__ == "__main__":
    main()