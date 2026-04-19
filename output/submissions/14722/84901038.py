import sys

input = sys.stdin.readline

def main():
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dp[i][j][graph[i][j]-1] != 0:
                dp[i][j][graph[i][j]] = max(dp[i][j][graph[i][j]],dp[i][j][graph[i][j]-1] + 1)
            if dp[i][j][0] == 0 and graph[i][j] == 0: dp[i][j][0] = 1
            for k in range(3):
                if dp[i][j][k] == 0: continue
                if i + 1 != n:
                    dp[i+1][j][k] = max(dp[i+1][j][k],dp[i][j][k])
                if j + 1 != n:
                    dp[i][j+1][k] = max(dp[i][j+1][k],dp[i][j][k])
    print(max(dp[n-1][n-1]))

if __name__ == "__main__":
    main()