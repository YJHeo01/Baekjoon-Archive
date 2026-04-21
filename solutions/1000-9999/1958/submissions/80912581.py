def main():
    print(get_LCS(list(input()),list(input()),list(input())))
    
def get_LCS(A,B,C):
    a_length = len(A)
    b_length = len(B)
    c_length = len(C)
    dp = [[[0] * (c_length+1) for _ in range(b_length+1)] for _ in range(a_length+1)]
    ret_value = []
    for i in range(a_length):
        for j in range(b_length):
            for k in range(c_length):
                if A[i] == B[j]:
                    dp[i+1][j+1][k+1] = dp[i][j][k] + 1
                else:
                    dp[i+1][j+1][k+1] = max(dp[i+1][j+1][k],dp[i+1][j][k+1],dp[i][j+1][k+1])
    return dp[a_length][b_length][c_length]
    dr = [-1,0,0]
    dc = [0,-1,0]
    dk = [0,0,-1]
    vr,vc,vk = a_length, b_length,c_length
    while True:
        nr, nc, nk = vr-1,vc-1, vk-1
        for i in range(3):
            r = vr + dr[i]
            c = vc + dc[i]
            k = vk + dk[i]
            if dp[r][c][k] == dp[vr][vc][vk]:
                nr,nc = r,c
                break
        if dp[vr][vc][vk] != dp[nr][nc][nk]:
            ret_value.append(A[nr])
        vr,vc,vk = nr,nc,nk
        if dp[vr][vc][vk] == 0:
            break
    ret_value.reverse()
    return ret_value

if __name__ == "__main__":
    main()