import sys, heapq

input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)+10)

INF = int(1e18)

def main():
    graph = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        edges.append((c,a,b))
        graph[a].append((b,c)); graph[b].append((a,c))
    edges.sort()
    
    tree = [[] for _ in range(n+1)]
    parent = list(range(n+1))
    special_node = set()
    for c,a,b in edges:
        if find_parent(parent,a) == find_parent(parent,b):
            special_node.add(b); special_node.add(a)
        else:
            tree[a].append((b,c)); tree[b].append((a,c))
            union_parent(parent,a,b)
    
    distance = [INF] * (n+1)
    distance = dijkstra(tree,distance,1)
    
    special_node = list(special_node)
    special_distance = []
    
    for node in special_node:
        special_distance.append(dijkstra(graph,[INF]*(n+1),node))
    
    parent = [[0]*(20) for _ in range(n+1)]
    depth = [-1] * (n+1)
    depth[1] = 0
    dfs(tree,depth,parent,1)
    set_parent(parent)
    
    q = int(input())
    l = len(special_node)

    for _ in range(q):
        a,b = map(int,input().split())
        lca = get_lca(parent,depth,a,b)
        answer = distance[a] + distance[b] - distance[lca]
        if lca == a: answer = distance[b] - distance[a]
        if lca == b: answer = distance[a] - distance[b]
        for i in range(l):
            answer = min(answer,special_distance[i][a]+special_distance[i][b])
        print(answer)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def dijkstra(graph,distance,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        d, x = heapq.heappop(q)
        if d != distance[x]: continue
        for nx, dd in graph[x]:
            nd = d + dd
            if nd >= distance[nx]: continue
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))
    return distance

def dfs(graph,depth,parent,vx):
    for nx,tmp in graph[vx]:
        if depth[nx] != -1: continue
        depth[nx] = depth[vx] + 1
        parent[nx][0] = vx
        dfs(graph,depth,parent,nx)

def set_parent(parent):
    for i in range(1,20):
        for j in range(n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def get_lca(parent,depth,a,b):
    if depth[a] > depth[b]: a,b = b,a
    tmp = 1 << 19
    for i in range(19,-1,-1):
        if depth[b] - depth[a] >= tmp:
            b = parent[b][i]
        tmp >>= 1
    if a == b: return a
    for i in range(19,-1,-1):
        if parent[a][i] != parent[b][i]:
            a,b = parent[a][i], parent[b][i]
    return parent[a][0]

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()