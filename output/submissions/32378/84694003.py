import sys

input = sys.stdin.readline

def main():
    mascot_size = solution()
    if mascot_size > 10 ** 11:
        print("MEGA")
    elif mascot_size <= 0:
        print("-1")
    else:
        print(mascot_size)

def solution():
    n,k,s = map(int,input().split())
    grow = list(map(int,input().split()))
    
    if k > 36:
        return 10 ** 11 + 1

    dp = [[0]*(k+1) for _ in range(n+1)]
    
    dp[0][0] = s
    
    for i in range(n):
        if dp[i][0] > 0:
            dp[i+1][0] = dp[i][0] + grow[i]
        for j in range(k):
            if dp[i][j] <= 0:
                continue
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + grow[i])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] * 2)
    
    return max(dp[n]) #n일차 횃불이가 가장 클 때의 사이즈

if __name__ == "__main__":
    main()