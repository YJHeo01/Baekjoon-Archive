A = [0] + list(input())
B = [0] + list(input())

len_A, len_B = len(A), len(B)
dp = [[0]*len_B for _ in range(len_A)]

for i in range(1,len_A):
    for j in range(1,len_B):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[len_A-1][len_B-1]) 