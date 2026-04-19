import sys,heapq

input = sys.stdin.readline

INF = int(1e10)

def main():
    graph = get_graph()
    distance = [[INF] * (k+1) for _ in range(n+1)]
    solution(graph,distance)
    answer = min(distance[n])
    print(answer)

def get_graph():
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    return graph

def solution(graph,distance):
    q = []
    heapq.heappush(q,(0,k,1))
    for i in range(k+1):
        distance[1][i] = 0
    while q:
        vt, cnt, vx = heapq.heappop(q)
        if vt > distance[vx][cnt]:
            continue
        for nx, dt in graph[vx]:
            nt = vt + dt
            if distance[nx][cnt] > nt:
                distance[nx][cnt] = nt
                heapq.heappush(q,(nt,cnt,nx))
            if cnt != 0:
                if distance[nx][cnt-1] > vt:
                    distance[nx][cnt-1] = vt
                    heapq.heappush(q,(vt,cnt-1,nx))

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    main()