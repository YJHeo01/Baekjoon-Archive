import sys

input = sys.stdin.readline

def main():
    n,t = map(int,input().split())
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    dp = [[0]*(t+1) for _ in range(n+1)]
    answer = 0
    for i in range(1,n+1):
        time, score = array[i-1]
        for j in range(1,t+1):
            if time > j: 
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-time]+score)
            answer = max(answer,dp[i][j])
    print(answer)

if __name__ == "__main__":
    main()