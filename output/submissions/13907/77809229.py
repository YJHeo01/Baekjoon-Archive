import sys,heapq

input = sys.stdin.readline

INF = int(1e12)

def main():
    graph = get_graph()
    distance = [[INF]*(n+1) for _ in range(n+1)]
    idx = dijkstra(graph,distance,s)
    distance = distance[d]
    answer = distance[idx]
    print(answer)
    path_list = get_path_list(distance,idx)
    tax(path_list)

def get_graph():
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,w = map(int,input().split())
        graph[a].append((b,w))
        graph[b].append((a,w))
    return graph

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,0,start))
    distance[start][0] = 0
    best_path_road_cnt = [0] * (n+1)
    while q:
        vd, visit_road_cnt, vx = heapq.heappop(q)
        if vd > distance[vx][visit_road_cnt]:
            continue
        for nx, dd in graph[vx]:
            nd = vd + dd
            if distance[nx][visit_road_cnt+1] > nd:
                if best_path_road_cnt[nx] < visit_road_cnt + 1:
                    if nd >= distance[nx][best_path_road_cnt[nx]]:
                        continue
                    best_path_road_cnt[nx] = visit_road_cnt + 1
                distance[nx][visit_road_cnt+1] = nd
                heapq.heappush(q,(nd,visit_road_cnt+1,nx))
    return best_path_road_cnt[d]

def get_path_list(distance,idx):
    ret_value = []
    for i in range(idx+1):
        if distance[i] >= INF:
            continue
        ret_value.append([distance[i],i])
    return ret_value

def tax(path_list):
    length = len(path_list)
    for _ in range(k):
        value = int(input())
        answer = INF; answer_idx = 0
        for i in range(length):
            path_list[i][0] += path_list[i][1] * value
            if answer > path_list[i][0]:
                answer = path_list[i][0]
                answer_idx = i
        print(answer)
        length = answer_idx + 1

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    s,d = map(int,input().split())
    main()