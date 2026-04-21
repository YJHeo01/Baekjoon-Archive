import sys
 
input = sys.stdin.readline
 
def main():
    answer = solution()
    print(answer)
 
def solution():
    n,k,s = map(int,input().split())
    array = list(map(int,input().split()))
    
    if k > 36:
        return "MEGA"
    
    if k == 0:
        for i in array:
            s += i
            if s <= 0:
                return -1
        return value_convert_answer(s)
 
    dp = [[-INF]*(k+1) for _ in range(n+1)]
    
    dp[0][0] = s
    
    for i in range(n):
        for j in range(k):
            if dp[i][j] <= 0:
                continue
            dp[i+1][j] = max(dp[i+1][j],dp[i][j] + array[i])
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j] * 2)
        if dp[i][k] > 0:
            dp[i+1][k] = max(dp[i+1][k],dp[i][k]+array[i])
    
    return value_convert_answer(max(dp[n]))
 
def value_convert_answer(value):
    if value > INF:
        return "MEGA"
    elif value <= 0:
        return -1
    else:
        return value
 
if __name__ == "__main__":
    INF = 100000000000
    main()
