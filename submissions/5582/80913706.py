def main():
    print(solution(list(input()),list(input())))

def solution(A,B):
    len_A = len(A)
    len_B = len(B)
    dp = [[0]*(len_B+1) for _ in range(len_A+1)]
    answer = 0
    for i in range(len_A):
        for j in range(len_B):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                answer = max(answer,dp[i+1][j+1])
    return answer

if __name__ == "__main__":
    main()