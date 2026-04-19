import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    study = [list(map(int,input().split())) for _ in range(k)]
    dp = [0] * (n+1)
    for i,t in study:
        for j in range(n,t-1,-1):
            dp[j] = max(dp[j],dp[j-t]+i)
    print(max(dp))

if __name__ == "__main__":
    main()