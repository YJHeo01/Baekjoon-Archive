import sys

input = sys.stdin.readline

def main():
    n,B,K = map(int,input().split())
    max_dp = [[[0]*n for _ in range(n)] for _ in range(B)]
    min_dp = [[[0]*n for _ in range(n)] for _ in range(B)]
    dx = [1,0,1]
    dy = [0,1,1]
    matrix = [list(map(int,input().split())) for _ in range(n)]
    
    idx = 0
    INF = n * n
    while True:
        if idx == INF: break
        i,j = idx//n, idx % n
        max_dp[0][i][j], min_dp[0][i][j] = matrix[i][j], matrix[i][j]
        idx += 1
    
    sum_x_y_list = list(range(2*n-2,-1,-1))
    
    for k in range(1,B): 
        for sum_x_y in sum_x_y_list:
            for x in range(max(0,sum_x_y-n+1),n):
                y = sum_x_y - x
                min_dp[k][x][y],max_dp[k][x][y] = matrix[x][y], matrix[x][y]
                for i in range(3):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= n or ny >= n: continue
                    max_dp[k][x][y] = max(max_dp[k][x][y],max_dp[k-1][nx][ny])
                    min_dp[k][x][y] = min(min_dp[k][x][y],min_dp[k-1][nx][ny])
    
    for _ in range(K):
        x,y = map(int,input().split())
        sys.stdout.write(str(max_dp[B-1][x-1][y-1]-min_dp[B-1][x-1][y-1])+'\n')
    
if __name__ == "__main__":
    main()