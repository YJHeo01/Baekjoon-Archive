import sys

input = sys.stdin.readline

def main():
    t = int(input())
    dp = [[0]*4 for _ in range(100001)]
    dp[1][1], dp[2][2], dp[3][3] = 1,1,1
    dp[3][1], dp[3][2] = 1,1
    for value in range(4,100001):
        for new_num in range(1,4):
            for last_num in range(1,4):
                if new_num == last_num: continue
                dp[value][new_num] += dp[value-new_num][last_num]
                dp[value][new_num] %= 1000000009
    for _ in range(t):
        n = int(input())
        answer = sum(dp[n]) % 1000000009
        print(answer)
        
if __name__ == "__main__":
    main()