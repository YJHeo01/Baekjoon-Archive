import sys

sys.setrecursionlimit(10**6)

def main():
    a,p = map(int,input().split())
    visited = [False] * 300000
    repeat_idx = search_repeat_start(p,visited,a)
    visited[repeat_idx] = True
    answer = get_answer(p,visited,a)
    print(answer)

def search_repeat_start(p,visited,vx):
    if visited[vx] == True: return vx
    visited[vx] = True
    nx = get_nx(p,vx)
    ret_value = search_repeat_start(p,visited,nx)
    visited[vx] = False
    return ret_value

def get_nx(p,vx):
    nx = 0
    while True:
        if vx == 0: break
        tmp = vx % 10
        nx += tmp ** p
        vx -= tmp
        vx = vx // 10
    return nx

def get_answer(p,visited,vx):
    if visited[vx] == True:
        return 0
    nx = get_nx(p,vx)
    return get_answer(p,visited,nx) + 1

if __name__ == "__main__":
    main()