from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    graph = get_graph(n)
    depth = get_depth(graph,n)
    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        if depth[a] > depth[b]: a,b = b,a
        print(solution(graph,depth,a,b))

def get_graph(n):
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def get_depth(graph,n):
    queue = deque([1])
    depth = [-1] * (n+1)
    depth[1] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if depth[nx] == -1:
                depth[nx] = depth[vx] + 1
                queue.append(nx)
    return depth

def solution(graph,depth,x,y):
    while True:
        if depth[x] == depth[y]:break
        y = get_new_idx(graph,depth,y)
    while True:
        if x == y: return x
        x = get_new_idx(graph,depth,x)
        y = get_new_idx(graph,depth,y)

def get_new_idx(graph,depth,idx):
    for ret_value in graph[idx]:
        if depth[ret_value] == depth[idx] - 1:
            return ret_value

if __name__ == "__main__":
    INF = 1000001
    main()