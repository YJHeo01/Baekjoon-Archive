def main():
    n = int(input())
    array = list(map(int,input().split()))
    dp = [0] * n
    answer = max(array)
    for i in range(n):
        for j in range(i+1,n):
            if array[i] > array[j] and dp[i] + array[i] > dp[j]:
                dp[j] = dp[i] + array[i]
                answer = max(answer,dp[j]+array[j])
    print(answer)

if __name__ == "__main__":
    main()