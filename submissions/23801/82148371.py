import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = get_graph(n,m)
    x,z = map(int,input().split())
    p = int(input())
    y = set(map(int,input().split()))
    distance = [[INF]*(2) for _ in range(n+1)]
    dijkstra(graph,distance,x,y)
    answer = distance[z][1]
    if answer >= INF:
        answer = -1
    print(answer)

def get_graph(n,m):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    return graph

def dijkstra(graph,distance,start,mid):
    q = []
    heapq.heappush(q,(0,0,start))
    distance[start][0] = 0
    while q:
        vd, cur_visited_mid, vx = heapq.heappop(q)
        if vd > distance[vx][cur_visited_mid]:
            continue
        for nx, dd in graph[vx]:
            next_visited_mid = cur_visited_mid
            if nx in mid:
                next_visited_mid = 1
            if distance[nx][next_visited_mid] > vd + dd:
                distance[nx][next_visited_mid] = vd + dd
                heapq.heappush(q,(vd+dd,next_visited_mid,nx))

if __name__ == "__main__":
    INF = 1000000 * 100000 + 1
    main()