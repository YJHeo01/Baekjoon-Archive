import sys, heapq
from itertools import permutations

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    x,z = map(int,input().split())
    p = int(input())
    y = [x] + list(map(int,input().split())) + [z]

    adj_matrix = []
    INF = int(1e14)
    for i in range(p+2):
        tmp = [INF] * (n+1)
        dijkstra(graph,tmp,y[i])
        p_iToP_j = []
        for j in range(p+2):
            p_iToP_j.append(tmp[y[j]])
        adj_matrix.append(p_iToP_j)
    
    test_case = list(permutations(list(range(1,p+1)),3))
    answer = INF
    for a,b,c in test_case:
        tmp = adj_matrix[0][a] + adj_matrix[a][b] + adj_matrix[b][c] + adj_matrix[c][p+1]
        answer = min(tmp,answer)
    if answer >= INF:
        answer = -1
    print(answer)

def dijkstra(graph,distance,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, w in graph[vx]:
            nd = dist + w
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))
    return distance
    
if __name__ == "__main__":
    main()