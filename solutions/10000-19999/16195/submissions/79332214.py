import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n,m = map(int,input().split())
        dp = [[0]*(m+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(1,4):
                if j > i:continue
                for k in range(1,m+1):
                    dp[i][k] += dp[i-j][k-1]
                    dp[i][k] %= 1000000009
        answer = sum(dp[n]) % 1000000009
        print(answer)

if __name__ == "__main__":
    main()