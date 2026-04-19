from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    distance = [INF] * (n+1)
    depth = [-1] * (n+1)
    parent = [[0]*20 for _ in range(n+1)]
    init(graph,distance,depth,parent)
    m = int(input())
    for _ in range(m):
        c, *tmp = input().split()
        if c == '1':
            u,v = map(int,tmp)
            lca = get_lca(parent,depth,u,v)
            print(distance[u]+distance[v]-2*distance[lca])
        else:
            u,v,k = map(int,tmp)
            lca = get_lca(parent,depth,u,v)
            k -= 1
            if depth[u] - depth[lca] >= k:
                print(query_two(parent,k,u))
            else:
                print(query_two(parent, depth[u] + depth[v] - 2* depth[lca]-k,v))

def init(graph,distance,depth,parent):
    queue = deque([1])
    depth[1], distance[1] = 0,0
    while queue:
        vx = queue.popleft()
        for nx, dd in graph[vx]:
            if depth[nx] == -1:
                parent[nx][0] = vx
                depth[nx] = depth[vx] + 1
                distance[nx] = distance[vx] + dd
                queue.append(nx)
    for i in range(1,20):
        for j in range(1,n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def get_lca(parent,depth,a,b):
    if depth[a] > depth[b]: a,b = b,a
    tmp = 1 << 19
    for i in range(19,-1,-1):
        if depth[b] - depth[a] >= tmp:
            b = parent[b][i]
        tmp >>= 1
    if a == b: return b
    for i in range(19,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

def query_two(parent,target_dist,cur_node):
    tmp = 1 << 19
    for i in range(19,-1,-1):
        if target_dist & tmp:
            cur_node = parent[cur_node][i]
        tmp >>= 1
    return cur_node

if __name__ == "__main__":
    INF = int(1e14)
    n = int(input())
    main()