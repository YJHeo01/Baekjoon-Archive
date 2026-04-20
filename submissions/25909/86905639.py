import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    move_list = [list(input().split()) for _ in range(n)]
    left, right = 1, 1000000
    answer = -1
    dx_dy = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    while left <= right:
        cur_time = 0
        x = (left+right) // 2
        cnt = 0
        visited = {}
        vx,vy = 0,0
        for a,b in move_list:
            dx,dy = dx_dy[a]
            for _ in range(int(b)):
                vx += dx; vy += dy; cur_time += 1
                if (vx,vy) not in visited:
                    visited[(vx,vy)] = cur_time
                elif cur_time - visited[(vx,vy)] >= x:
                    cnt += 1
                    visited[(vx,vy)] = cur_time
        if cnt >= k:
            answer = x
            left = x + 1
        else:
            right = x - 1
    print(answer)
                
if __name__ == "__main__":
    main()