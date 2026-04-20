from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    global d
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
    if d != 0:
        for i in range(1,n+1):
            if edge_cnt[i] == 1:
                visited[i] = 1
                get_power_area(tree,depth,visited,i,d)
    answer = solution(tree,depth,visited,s)
    if answer != 0: answer -= 1
    answer *= 2
    print(answer)

def get_depth(graph,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == -1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

def get_power_area(tree,depth,visited,vx,limit):
    if visited[vx] == limit: return
    for nx in tree[vx]:
        if depth[nx] > depth[vx]: continue
        visited[nx] = visited[vx] + 1
        get_power_area(tree,depth,visited,nx,limit)


def solution(tree,depth,visited,vx):
    ret_value = 0
    if visited[vx] != INF:
        init_ret_value = 0
    else:
        init_ret_value = 1
    visited[vx] = 0
    for nx in tree[vx]:
        if visited[nx] == 0:continue
        ret_value += solution(tree,depth,visited,nx)
    if ret_value != 0 and init_ret_value == 0:
        ret_value += 1
    ret_value += init_ret_value
    return ret_value

if __name__ == "__main__":
    INF = int(1e9)
    main()