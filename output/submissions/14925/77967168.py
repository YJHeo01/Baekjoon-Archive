import sys

input = sys.stdin.readline

def main():
    ground = get_ground()
    answer = get_answer(ground)
    print(answer)

def get_ground():
    ground = []
    for _ in range(m):
        ground.append(list(map(int,input().split())))
    return ground

def get_answer(ground):
    dp = get_init_dp(ground)
    answer = max(max(dp[0]),max(dp[:][0]))
    for i in range(1,m):
        for j in range(1,n):
            if ground[i][j] != 0:
                continue
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
            answer = max(answer,dp[i][j])
    return answer

def get_init_dp(ground):
    dp = [[0]*n for _ in range(m)]
    for i in range(m):
        if ground[i][0] != 0:
            continue
        dp[i][0] = 1
    for i in range(n):
        if ground[0][i] != 0:
            continue
        dp[0][i] = 1
    return dp

if __name__ == "__main__":
    m,n = map(int,input().split())
    main()