import sys

input = sys.stdin.readline

def main():
    n,B,K = map(int,input().split())
    max_dp = [[[0]*B for _ in range(n)] for _ in range(n)]
    min_dp = [[[0]*B for _ in range(n)] for _ in range(n)]
    dx = [1,0,1]
    dy = [0,1,1]
    matrix = [list(map(int,input().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            max_dp[i][j][0], min_dp[i][j][0] = matrix[i][j], matrix[i][j]
    
    for k in range(1,B): 
        for sum_x_y in range(2*n-2,-1,-1):
            for x in range(max(0,sum_x_y-n+1),n):
                y = sum_x_y - x
                min_dp[x][y][k],max_dp[x][y][k] = matrix[x][y], matrix[x][y]
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