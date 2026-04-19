def main():
    print(solution(list(input()),list(input())))

def solution(A,B):
    a_length = len(A); b_length = len(B)
    dp = [[0]*(b_length+1) for _ in range(a_length+1)]
    for i in range(a_length):
        for j in range(b_length):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    return a_length + b_length - dp[a_length][b_length]

if __name__ == "__main__":
    main()