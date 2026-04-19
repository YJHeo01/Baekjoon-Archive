from collections import deque
import sys

input = sys.stdin.readline

def main():
    xs,ys = map(int,input().split())
    t = int(input())
    xh,yh = map(int,input().split())
    block = [[False]*(2*t+1) for _ in range(2*t+1)]
    n = int(input())
    for _ in range(n):
        xi,yi = map(int,input().split())
        x = xi - xs + t
        y = yi - ys + t
        if x < 0 or y < 0 or x > 2 * t or y > 2 * t:continue
        block[x][y] = True
    cnt = [[[0]*(t+1) for _ in range(2*t+1)] for _ in range(2*t+1)]
    target = (t + xh - xs, t + yh - ys)
    print(solution(block,cnt,t,target))
    
def solution(block,cnt,t,target):
    queue = deque([(t,t,0)])
    cnt[t][t][0] = 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy, vt = queue.popleft()
        nt = vt + 1
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx > 2 * t or ny > 2 * t or block[nx][ny]:continue
            cnt[nx][ny][nt] += cnt[vx][vy][vt]
            cnt[nx][ny][nt] %= 10 ** 9 + 7
            if nt == t or (target[0]==nx and target[1] == ny):
                continue
            queue.append((nx,ny,nt))
    if target[0] < 0 or target[1] < 0 or target[0] > 2 * t or target[1] > 2 * t:
        return 0
    ret_value = 0
    for i in range(t+1):
        ret_value += cnt[target[0]][target[1]][i]
        ret_value %= 10 ** 9 + 7
    return ret_value
    
if __name__ == "__main__":
    main()