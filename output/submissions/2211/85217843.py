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
    answer = dijkstra(graph,distance)
    print(len(answer))
    for i in answer:
        print(*i)

def dijkstra(graph,distance):
    q = []
    heapq.heappush(q,(0,0,1))
    distance[1] = 0
    ret_value = []
    while q:
        dist, last_node, cur_node = heapq.heappop(q)
        if dist > distance[cur_node]:
            continue
        ret_value.append([last_node,cur_node])
        for next_node, dd in graph[cur_node]:
            if distance[next_node] > dist + dd:
                distance[next_node] = dist + dd
                heapq.heappush(q,(dist+dd,cur_node,next_node))
    return ret_value[1:]

if __name__ == "__main__":
    INF = int(1e9)
    main()