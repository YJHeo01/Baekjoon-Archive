import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[]for _ in range(n+1)]
    new_oil_price = [0] + list(map(int,input().split()))
    for _ in range(m):
        a,b,length = map(int,input().split())
        graph[a].append((b,length))
        graph[b].append((a,length))
    price = [[INF]*2501 for _ in range(n+1)]
    dijkstra(graph,new_oil_price,price)
    answer = min(price[n])
    print(answer)
    
def dijkstra(graph,new_oil_price,node_price):
    q = []
    heapq.heappush(q,(0,2500,1))
    node_price[1][0] = 0
    node_price[1][2500] = 0
    while q:
        sum_price, min_price, vx = heapq.heappop(q)
        if sum_price > node_price[vx][min_price]: continue
        next_min_price = min(new_oil_price[vx],min_price)
        for nx, length in graph[vx]:
            next_sum_price = sum_price + length * next_min_price
            if node_price[nx][next_min_price] > next_sum_price:
                node_price[nx][next_min_price] = next_sum_price
                heapq.heappush(q,(next_sum_price,next_min_price,nx))

if __name__ == "__main__":
    INF = int(1e9)
    main()