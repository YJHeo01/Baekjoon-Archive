import sys

input = sys.stdin.readline

def main():
    array = get_array(n)
    answer = solution(array)
    print(answer)

def get_array(n):
    array = []
    for _ in range(n):
        array.append(list(input()))
    return array

def solution(array):
    dp = get_init_dp(array)
    ret_value = max(max(dp[0],dp[:][0]))
    for i in range(1,n):
        for j in range(1,m):
            if array[i][j] == '0': continue
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + 1
            ret_value = max(ret_value,dp[i][j])
    ret_value *= ret_value
    return ret_value

def get_init_dp(array):
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        if array[i][0] == '0': continue
        dp[i][0] = 1
    for i in range(1,m):
        if array[0][i] == '0': continue
        dp[0][i] = 1
    return dp

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()