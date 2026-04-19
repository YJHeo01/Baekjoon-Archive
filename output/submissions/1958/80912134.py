def main():
    s_A = list(input())
    s_B = list(input())
    s_C = list(input())
    print(len(get_LCS(get_LCS(s_A,s_B),s_C)))
    
def get_LCS(A,B):
    a_length = len(A)
    b_length = len(B)
    dp = [[0]*(b_length+1) for _ in range(a_length+1)]
    ret_value = []
    for i in range(a_length):
        for j in range(b_length):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    dr = [-1,0]
    dc = [0,-1]
    vr,vc = a_length, b_length
    while True:
        nr, nc = vr-1,vc-1
        for i in range(2):
            r = vr + dr[i]
            c = vc + dc[i]
            if dp[r][c] == dp[vr][vc]:
                nr,nc = r,c
                break
        if dp[vr][vc] != dp[nr][nc]:
            ret_value.append(A[nr])
        vr,vc = nr,nc
        if dp[vr][vc] == 0:
            break
    ret_value.reverse()
    return ret_value

if __name__ == "__main__":
    main()