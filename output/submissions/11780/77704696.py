import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    bus, reverse_bus = get_bus(n)
    distance = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1): 
        dijkstra(bus,distance[i],i)
    print_cost(distance)
    for i in range(1,n+1):
        print_path(reverse_bus,distance[i],i)
        
def get_bus(n):
    bus = [[] for _ in range(n+1)]
    reverse_bus = [[]for _ in range(n+1)]
    m = int(input())
    for _ in range(m):
        a,b,c = map(int,input().split())
        bus[a].append((b,c))
        reverse_bus[b].append((a,c))
    return bus, reverse_bus

def dijkstra(graph,distance,start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(dist+length,nx))

def print_cost(distance):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] == INF:
                print(0,end=" ")
            else:
                print(distance[i][j],end=" ")
        print()

def print_path(graph,distance,start):
    for i in range(1,n+1):
        if distance[i] == INF or start == i:
            print(0)
            continue
        path = get_path(graph,distance,start,i)
        print(len(path),end=" ")
        for city in path:
            print(city,end=" ")
        print()

def get_path(graph,distance,start,end):
    ret_value = [end]
    vx = end
    while True:
        for nx,length in graph[vx]:
            if distance[nx] + length == distance[vx]:
                ret_value = [nx] + ret_value
                break
        if nx == start:
            break
        vx = nx
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()