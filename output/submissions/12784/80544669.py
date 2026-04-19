import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()

def solution():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    depth = [-1] * (n+1)
    depth[1] = 0
    get_depth(graph,depth,1)
    print(get_cnt(graph,depth,1))

def get_depth(graph,depth,vx):
    for nx,d in graph[vx]:
        if depth[nx] == -1:
            depth[nx] = depth[vx] + 1
            get_depth(graph,depth,nx)

def get_cnt(graph,depth,vx):
    if len(graph[vx]) == 1:
        return graph[vx][0][1]
    ret_value_A = 0
    ret_value_B = 0
    for nx,d in graph[vx]:
        if depth[nx] > depth[vx]:
            ret_value_A += get_cnt(graph,depth,nx)
        else:
            ret_value_B += d
    if vx == 1:
        return ret_value_A
    return min(ret_value_A,ret_value_B)

if __name__ == "__main__":
    main()