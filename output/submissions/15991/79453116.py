import sys

input = sys.stdin.readline

def main():
    dp = [0] * (50001)
    dp[0], dp[1], dp[2] = 1,1,2
    for i in range(3,50001):
        for plus in range(1,4):
            dp[i] += dp[i-plus]
            dp[i] %= 1000000009
    t = int(input())
    for _ in range(t):
        n = int(input())
        answer = 0
        for i in range(4):
            if i > n: break
            if (n-i) % 2 == 0:
                answer += dp[(n-i)//2]
        answer %= 1000000009
        print(answer)

if __name__ == "__main__":
    main()