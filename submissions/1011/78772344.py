import sys

sys.setrecursionlimit(10**6)

def main():
    t = int(input())
    for _ in range(t):
        a,b = map(int,input().split())
        print(move(0,a,b,0))

def move(last_move,vx,end,move_cnt):
    if vx == end:
        if last_move == 1: return move_cnt
        else: return INF
    ret_value = INF
    for dx in [1,0,-1]:
        cur_move = last_move + dx
        nx = vx + cur_move
        if nx > end: continue
        ret_value = move(cur_move,nx,end,move_cnt + 1)
        if ret_value != INF:
            break
    return ret_value

if __name__ == "__main__":
    INF = int(1e9)
    main()