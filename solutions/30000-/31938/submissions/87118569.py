#다익스트라
#?번 도시의 최단 경로 중 ?번 도시에 방문하기 직전 도시를 체크한다.
#최단경로가 2가지 이상인 경우, 직전 도시의 최단 경로가 더 긴 곳을 직전 도시로 저장한다.
#직전도시까지는 트럭 군집주행을 통해 운송비를 10% 절약하고, 직전 도시 - ?번 도시의 거리만 운송비를 그대로 지출한다.

import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    distance = [INF] * (n+1)
    last_visit_city = [0] * (n+1)
    answer = 0
    dijkstra(graph,distance,last_visit_city)
    for i in range(2,n+1):
        answer += (distance[i] - distance[last_visit_city[i]] // 10)
    print(answer)

def dijkstra(graph,distance,last_visit_city):
    q = []
    distance[1] = 0
    heapq.heappush(q,(0,1))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, dd in graph[vx]:
            nd = dist + dd
            if distance[nx] < nd: continue
            if distance[nx] > nd:
                last_visit_city[nx] = vx
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))
            else:
                if distance[last_visit_city[nx]] < distance[vx]:
                    last_visit_city[nx] = vx

if __name__ == "__main__":
    INF = int(1e13)
    main()