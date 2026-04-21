import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
    x,y,z = map(int,input().split())
    INF = int(1e9) * 2 + 1
    distance = [[INF]*2 for _ in range(n+1)]
    solution(graph,distance,x,y)
    y_not_visit_distance, y_visit_distance = distance[z]
    if y_not_visit_distance >= INF: y_not_visit_distance = -1
    if y_visit_distance >= INF: y_visit_distance = -1
    print(y_visit_distance,y_not_visit_distance)

def solution(graph,distance,start,mid):
    q = []
    distance[start][0] = 0
    heapq.heappush(q,(0,0,start))
    while q:
        dist, visit_mid, vx = heapq.heappop(q)
        if dist > distance[vx][visit_mid]:
            continue
        for nx, w in graph[vx]:
            next_visit_mid = visit_mid
            if nx == mid: next_visit_mid = 1
            next_dist = dist + w
            if distance[nx][next_visit_mid] > next_dist:
                distance[nx][next_visit_mid] = next_dist
                heapq.heappush(q,(next_dist,next_visit_mid,nx))

if __name__ == "__main__":
    main()