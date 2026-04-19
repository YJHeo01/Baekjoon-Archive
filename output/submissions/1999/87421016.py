#동적계획법
#B가 N과 같다고 가정할 경우 제가 계산한 시간복잡도는 O(N^3)
#N의 제한이 250이므로, O(N^3)이어도 통과 가능하다고 판단, 그러나 TLE 판정

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
    
    for k in range(1,B): #좌측 상단이 (x,y)이고, 부분 행렬의 크기가 (k+1)일때 최대, 최소
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
        answer = max_dp[x-1][y-1][B-1] - min_dp[x-1][y-1][B-1]
        print(answer)

if __name__ == "__main__":
    main()