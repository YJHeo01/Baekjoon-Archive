import sys,heapq

input = sys.stdin.readline

def main():
    graph = get_graph()
    answer = binary_search(graph)
    if answer >= INF:
        answer = -1
    print(answer)

def get_graph():
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    return graph

def binary_search(graph):
    answer = INF
    left = 0; right = c
    while left <= right:
        mid = (left+right) // 2
        distance = [INF] * (n+1)
        dijkstra(graph,distance,mid)
        if distance[b] >= INF:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer

def dijkstra(graph,distance,limit):
    q = []
    heapq.heappush(q,(0,a))
    distance[a] = 0
    while q:
        sum_cost, vx = heapq.heappop(q)
        if sum_cost > distance[vx]:
            continue
        for nx, cost in graph[vx]:
            next_sum_cost = sum_cost + cost
            if cost > limit:
                continue
            if distance[nx] > next_sum_cost:
                distance[nx] = next_sum_cost
                heapq.heappush(q,(next_sum_cost,nx))

if __name__ == "__main__":
    n,m,a,b,c = map(int,input().split())
    INF = c+1
    main()