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
    visited = [-1] * (n+1)
    answer = 0
    start = []
    for i in range(1,n+1):
        if edge_cnt[i] == 1 and depth[i] > d and i != s:
            heapq.heappush(start,(-depth[i],i))
    while start:
        t, idx = heapq.heappop(start)
        visited[idx] = 0
        tmp = dfs(tree,depth,visited,idx) - d
        if tmp > 0: answer += tmp
    answer *= 2
    print(answer)

def get_depth(graph,depth,start):
    queue = deque([start])
    depth[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if depth[nx] == -1:
                depth[nx] = depth[vx] + 1
                queue.append(nx)

def dfs(graph,depth,visited,vx):
    for nx in graph[vx]:
        if visited[nx] == -1 and depth[nx] < depth[vx]:
            visited[nx] = visited[vx] + 1
            return dfs(graph,depth,visited,nx)
    return visited[vx]
        
if __name__ == "__main__":
    main()