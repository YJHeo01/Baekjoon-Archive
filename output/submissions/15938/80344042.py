import sys

input = sys.stdin.readline

def main():
    xs,ys = map(int,input().split())
    t = int(input())
    xh,yh = map(int,input().split())
    house_x, house_y = t + xh - xs, t + yh - ys
    block = [[False]*(2*t+1) for _ in range(2*t+1)]
    n = int(input())
    for _ in range(n):
        xi,yi = map(int,input().split())
        x = xi - xs + t
        y = yi - ys + t
        if x < 0 or y < 0 or x > 2 * t or y > 2 * t:continue
        block[x][y] = True
    cnt = [[[0]*(t+1) for _ in range(2*t+1)] for _ in range(2*t+1)]
    cnt[t][t][0] = 1
    length = 2 * t + 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    answer = 0
    modular_value = 10**9 + 7
    for vt in range(t):
        for vx in range(t-vt-1,t+vt+2):
            for vy in range(t-vt-1,t+vt+2):
                if block[vx][vy] == True: continue
                for i in range(4):
                    nx = vx + dx[i]
                    ny = vy + dy[i]
                    if nx < 0 or ny < 0 or nx >= length or ny >= length: continue
                    if nx == house_x and ny == house_y: continue
                    cnt[vx][vy][vt+1] += cnt[nx][ny][vt]
                    cnt[vx][vy][vt+1] %= modular_value
                if vx == house_x and vy == house_y:
                    answer += cnt[vx][vy][vt+1]
                    answer %= modular_value
    print(answer)
                
if __name__ == "__main__":
    main()