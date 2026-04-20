import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    price = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    distnace = [[INF]*(2501) for _ in range(n+1)]
    city_min_new_price = [2500] * (n+1)
    dijkstra(graph,distnace,price,city_min_new_price)
    answer = min(distnace[n])
    print(answer)
    
def dijkstra(graph,distance,new_price,best_price_of_city):
    q = []
    heapq.heappush(q,(0,new_price[1],1))
    distance[1][new_price[1]] = 0
    while q:
        dist, best_price, vx = heapq.heappop(q)
        if dist > distance[vx][best_price] or dist > distance[vx][best_price_of_city[vx]]:
            continue
        new_best_price = min(best_price,new_price[vx])
        for nx, length in graph[vx]:
            new_dist = dist + new_best_price * length
            if distance[nx][new_best_price] > new_dist:
                best_price_of_city[nx] = min(best_price_of_city[nx],new_best_price)
                distance[nx][new_best_price] = new_dist
                heapq.heappush(q,(new_dist,new_best_price,nx))

if __name__ == "__main__":
    INF = int(1e9)
    main()