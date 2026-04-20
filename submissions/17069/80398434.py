import sys

input = sys.stdin.readline

def main():
    n = int(input())
    house = get_house(n)
    dp = [[[0]*3 for _ in range(n)]for _ in range(n)]
    dp[0][1][0] = 1
    dx = [0,1,1]; dy = [1,1,0]
    
    for vx in range(n):
        for vy in range(n):
            if house[vx][vy] == 1:continue
            for vd in range(3):
                for i in range(-1,2):
                    nd = vd + i
                    if nd < 0 or nd >= 3: continue
                    nx = vx + dx[nd]
                    ny = vy + dy[nd]
                    if nx >= n or ny >= n or house[nx][ny] == 1: continue
                    if nd == 1 and (house[vx+1][vy] == 1 or house[vx][vy+1]): continue
                    dp[nx][ny][nd] += dp[vx][vy][vd]
    
    print(sum(dp[n-1][n-1]))

def get_house(n):
    house = []
    for _ in range(n):
        house.append(list(map(int,input().split())))
    return house

if __name__ == "__main__":
    main()