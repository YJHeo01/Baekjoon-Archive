import sys

input = sys.stdin.readline

def main():
    n,t = map(int,input().split())
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    dp = [[-1]*(t+1) for _ in range(n+1)]
    dp[0][0] = 0
    answer = 0
    for i in range(n):
        time, score = array[i]
        if time > t: continue
        for j in range(t+1-time):
            if dp[i][j] != -1:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j])
                dp[i+1][j+time] = max(dp[i][j]+score,dp[i+1][j+time])
                answer = max(answer,dp[i+1][j+time])
    print(answer)

if __name__ == "__main__":
    main()