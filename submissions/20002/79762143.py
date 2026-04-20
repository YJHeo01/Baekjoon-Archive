import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    prefix_sum_h = [[0] * (n+1) for _ in range(n+1)]
    prefix_sum_w = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            prefix_sum_h[i][j] = prefix_sum_h[i-1][j] + array[i-1][j-1]
            prefix_sum_w[i][j] = prefix_sum_w[i][j-1] + array[i-1][j-1]
    
    answer = -1000
    
    dp = [[[0]*n for _ in range(n)]for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            dp[0][i][j] = array[i][j]
            answer = max(answer,array[i][j])

    for k in range(1,n):
        for i in range(k,n):
            for j in range(k,n):
                dp[k][i][j] = dp[k-1][i-1][j-1] 
                dp[k][i][j] += prefix_sum_h[i+1][j+1] - prefix_sum_h[i-k][j+1] 
                dp[k][i][j] += prefix_sum_w[i+1][j+1] - prefix_sum_w[i+1][j-k] 
                dp[k][i][j] -= array[i][j]
                answer = max(answer,dp[k][i][j])
    print(answer)

if __name__  == "__main__":
    main()