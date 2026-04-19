import sys

input = sys.stdin.readline

def main():
    xs,ys = map(int,input().split())
    t = int(input())
    xh,yh = map(int,input().split())
    house_x, house_y = t + xh - xs, t + yh - ys
    if house_x < 0 or house_y < 0 or house_x > 2 * t or house_y > 2 * t:
        print(0)
        return
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
        for vx in range(max(0,house_x-t+vt,t-vt),min(length,house_x+t-vt+1,t+vt+1)):
            for vy in range(max(0,house_y-t+vt,t-vt),min(length,house_y+t-vt+1,t+vt+1)):
                if cnt[vx][vy][vt] == 0: continue
                if vx == house_x and vy == house_y:
                    answer += cnt[vx][vy][vt]
                    answer %= modular_value
                    continue
                for i in range(4):
                    nx = vx + dx[i]
                    ny = vy + dy[i]
                    if nx < 0 or ny < 0 or nx >= length or ny >= length or block[nx][ny]: continue
                    cnt[nx][ny][vt+1] += cnt[vx][vy][vt]
                    cnt[nx][ny][vt+1] %= modular_value
    answer = (answer+cnt[house_x][house_y][t]) % modular_value
    print(answer)
                
if __name__ == "__main__":
    main()