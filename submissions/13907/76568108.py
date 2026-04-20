import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

n,m,k = map(int,input().split())

s,d = map(int,input().split())

graph = [[] for _ in range(n+1)]

distance = [[INF]*(n+1) for _ in range(n)]

for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,0,start))
    distance[0][start] = 0
    ret_value_min = INF
    ret_value_max = 0
    while q:
        vd, visit_road_cnt, vx = heapq.heappop(q)
        if vx == d:
            ret_value_max = max(ret_value_max,visit_road_cnt)
            ret_value_min = min(ret_value_min,visit_road_cnt)
            continue
        if vd > distance[visit_road_cnt][vx]:
            continue
        for nx, dd in graph[vx]:
            nd = vd + dd
            if distance[visit_road_cnt+1][nx] > nd:
                distance[visit_road_cnt+1][nx] = nd
                if visit_road_cnt >= 1 and distance[visit_road_cnt-1][nx] == vd - dd:
                    continue
                heapq.heappush(q,(nd,visit_road_cnt+1,nx))
    return (ret_value_min, ret_value_max + 1)

answer = INF

start, end = dijkstra(graph,distance,s)

answer_idx = end
for i in range(start,end):
    if answer > distance[i][d]:
        answer = distance[i][d]
        answer_idx = i

print(answer)

end = answer_idx + 1

for _ in range(k):
    tmp = int(input())
    answer = INF
    for i in range(start,end):
        distance[i][d] += tmp * i
        if answer > distance[i][d]:
            answer = distance[i][d]
            answer_idx = i
    print(answer)
    end = answer_idx + 1