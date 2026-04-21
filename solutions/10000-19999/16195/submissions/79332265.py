import sys

input = sys.stdin.readline

def main():
    t = int(input())
    dp = [[0]*1001 for _ in range(1001)]
    dp[0][0] = 1
    for i in range(1,1001):
        for j in range(1,4):
            if j > i:continue
            for k in range(1,1001):
                dp[i][k] += dp[i-j][k-1]
                dp[i][k] %= 1000000009    
    for _ in range(t):
        n,m = map(int,input().split())
        answer = sum(dp[n][:m+1]) % 1000000009
        print(answer)

if __name__ == "__main__":
    main()