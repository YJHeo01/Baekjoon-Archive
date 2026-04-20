from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    depth = [-1] * (n+1)
    distance = [0] * (n+1)
    parent = [[0]*20 for _ in range(n+1)]
    init(graph,depth,distance,parent)
    m = int(input())
    for _ in range(m):
        idx, *tmp = input().split()
        if idx == '1':
            u,v = map(int,tmp)
            lca = get_lca(parent,depth,u,v)
            print(distance[u]+distance[v]-2*distance[lca])
        else:
            u,v,k = map(int,tmp)
            lca = get_lca(parent,depth,u,v)
            k -= 1
            if depth[u] - depth[lca] > k:
                print(get_node(parent,depth,depth[u]-depth[lca]-k,lca,u))
            elif depth[u] - depth[lca] < k:
                print(get_node(parent,depth,depth[v]-depth[lca]-(k-depth[u]+depth[lca]),lca,v))
            else:
                print(lca)
            

def init(graph,depth,distance,parent):
    queue = deque([1])
    depth[1] = 0
    while queue:
        vx = queue.popleft()
        for nx, w in graph[vx]:
            if depth[nx] != -1: continue
            parent[nx][0] = vx
            depth[nx] = depth[vx] + 1
            distance[nx] = distance[vx] + w
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
    if a == b:
        return a
    for i in range(19,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

def get_node(parent,depth,target_dist,a,b):
    tmp = 1 << 19
    for i in range(19,-1,-1):
        if depth[b] - depth[a] - tmp >= target_dist:
            b = parent[b][i]
        tmp >>= 1
    return b

if __name__ == "__main__":
    n = int(input())
    main()