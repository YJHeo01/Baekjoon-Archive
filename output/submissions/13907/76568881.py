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
    ret_value = [False] * n
    while q:
        vd, visit_road_cnt, vx = heapq.heappop(q)
        if vd > distance[visit_road_cnt][vx]:
            continue
        if vx == d:
            ret_value[visit_road_cnt] = True
            continue
        for nx, dd in graph[vx]:
            nd = vd + dd
            if distance[visit_road_cnt+1][nx] > nd:
                distance[visit_road_cnt+1][nx] = nd
                if visit_road_cnt >= 1 and distance[visit_road_cnt-1][nx] == vd - dd:
                    continue
                heapq.heappush(q,(nd,visit_road_cnt+1,nx))
    return ret_value

answer = INF

city_cnt_list = dijkstra(graph,distance,s)

length = 0
test_case = []

for i in range(n):
    if city_cnt_list[i] == True:
        test_case.append(i)
        length += 1
        if answer > distance[i][d]:
            answer = distance[i][d]

print(answer)

for _ in range(k):
    tmp = int(input())
    answer = INF
    for i in range(length):
        cnt = test_case[i]
        distance[cnt][d] += tmp * cnt
        if answer > distance[cnt][d]:
            answer = distance[cnt][d]
            answer_idx = i
    print(answer)
    length = answer_idx + 1