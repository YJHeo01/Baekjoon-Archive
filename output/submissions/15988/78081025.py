import sys

input = sys.stdin.readline

def main():
    t = int(input())
    dp = get_dp()
    for _ in range(t):
        num = int(input())
        answer = dp[num]
        print(answer)

def get_dp():
    dp_size = 1000001
    dp = [0] * dp_size
    for i in range(1,4):
        dp[i] = 2 ** (i-1)
    for i in range(4,dp_size):
        dp[i] += (dp[i-1]+dp[i-2]+dp[i-3])
        dp[i] %= 1000000009
    return dp

if __name__ == "__main__":
    main()