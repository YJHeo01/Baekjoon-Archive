import sys

sys.setrecursionlimit(10**6)

def main():
    t = int(input())
    for _ in range(t):
        a,b = map(int,input().split())
        b = b - a
        print(move(0,0,b,0))

def move(last_move,vx,end,move_cnt):
    if vx == end:
        if last_move == 1: return move_cnt
        else: return INF
    if vx >= (end // 2) + 1:
        dx_list = [0,-1]
    else:
        dx_list = [1,0]
    ret_value = INF
    for dx in dx_list:
        cur_move = last_move + dx
        if cur_move <= 0: continue
        nx = vx + cur_move
        if nx > end: continue
        ret_value = move(cur_move,nx,end,move_cnt + 1)
        if ret_value != INF: break
    return ret_value

if __name__ == "__main__":
    INF = int(1e9)
    main()