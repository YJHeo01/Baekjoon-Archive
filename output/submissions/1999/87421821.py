import sys

input = sys.stdin.readline

def main():
    n,B,K = map(int,input().split())
    max_dp = [[[0]*B for _ in range(n)] for _ in range(n)]
    min_dp = [[[0]*B for _ in range(n)] for _ in range(n)]
    dx = [1,0,1]
    dy = [0,1,1]
    matrix = []
    
    for _ in range(n):
        matrix += list(map(int,input().split()))
    
    idx = 0
    INF = n * n
    while True:
        if idx == INF: break
        i,j = idx//n, idx % n
        max_dp[i][j][0], min_dp[i][j][0] = matrix[idx], matrix[idx]
        idx += 1
    
    sum_x_y_list = list(range(2*n-2,-1,-1))
    
    for k in range(1,B): 
        for sum_x_y in sum_x_y_list:
            for x in range(max(0,sum_x_y-n+1),n):
                y = sum_x_y - x
                idx = x * n + y
                min_dp[x][y][k],max_dp[x][y][k] = matrix[idx], matrix[idx]
                for i in range(3):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= n or ny >= n: continue
                    max_dp[x][y][k] = max(max_dp[x][y][k],max_dp[nx][ny][k-1])
                    min_dp[x][y][k] = min(min_dp[x][y][k],min_dp[nx][ny][k-1])
    
    for _ in range(K):
        x,y = map(int,input().split())
        sys.stdout.write(str(max_dp[x-1][y-1][B-1]-min_dp[x-1][y-1][B-1])+'\n')
    
if __name__ == "__main__":
    main()