from collections import deque
import sys, heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n,s,d = map(int,input().split())
    tree = [[] for _ in range(n+1)]
    edge_cnt = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
        edge_cnt[a] += 1
        edge_cnt[b] += 1
    depth = [-1] * (n+1)
    get_depth(tree,depth,s)
    visited = [INF] * (n+1)
    q = []
    for i in range(1,n+1):
        if d == 0:
            break
        if edge_cnt[i] == 1 or i == s:
            visited[i] = 1
            get_power_area(tree,visited,i,d)
    answer = solution(tree,visited,s)
    if answer != 0: answer -= 1
    answer *= 2
    print(answer)

def get_power_area(tree,visited,vx,limit):
    if visited[vx] == limit:
        return
    for nx in tree[vx]:
        if visited[vx] + 1 >= visited[nx]: continue
        visited[nx] = visited[vx] + 1
        get_power_area(tree,visited,nx,limit)

def get_depth(tree,depth,start):
    queue = deque([start])
    depth[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in tree[vx]:
            if depth[nx] == -1:
                depth[nx] = depth[vx] + 1
                queue.append(nx)

def solution(tree,visited,vx):
    ret_value = 0
    if visited[vx] != INF:
        init_ret_value = 0
    else:
        init_ret_value = 1
    visited[vx] = 0
    for nx in tree[vx]:
        if visited[nx] == 0:continue
        ret_value += solution(tree,visited,nx)
    if ret_value != 0 and init_ret_value == 0:
        ret_value += 1
    ret_value += init_ret_value
    return ret_value

if __name__ == "__main__":
    INF = int(1e9)
    main()