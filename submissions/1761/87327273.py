#최소 공통 조상
#1을 루트로 삼고 두 노드를 a,b 라고 표현할 때, dist[a] + dist[b] - 2 * dist[lca]
#트리이므로, 데이크스트라를 사용할 필요 없이, bfs만으로도 최단 경로 계산 가능

from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    depth = [-1] * (n+1)
    parent = [[0]*20 for _ in range(n+1)]
    distance = [-1] * (n+1)
    init(graph,depth,parent,distance)

    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        lca = get_lca(parent,depth,a,b)
        print(distance[a]+distance[b] - 2 * distance[lca])

def init(graph,depth,parent,distance):
    queue = deque([1])
    depth[1] = 0
    distance[1] = 0
    while queue: #depth,distance 게산을 위한 bfs
        vx = queue.popleft()
        for nx,dd in graph[vx]:
            if depth[nx] == -1:
                depth[nx] = depth[vx] + 1
                distance[nx] = distance[vx] + dd
                parent[nx][0] = vx
                queue.append(nx)
    
    for i in range(1,20): #lca를 위한 for문
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
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

if __name__ == "__main__":
    INF = int(1e9)
    n = int(input())
    main()
