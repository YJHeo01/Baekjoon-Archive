import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    global n,m,k
    n,m,k = map(int,input().split())
    graph = get_graph()
    distance = [[INF]*k for _ in range(n+1)]
    k -= 1
    solution(graph,distance)
    print_answer(distance)

def get_graph():
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
    return graph

def solution(graph,distance):
    q = []
    heapq.heappush(q,(0,1))
    distance[1][0] = 0
    while q:
        vt, vx = heapq.heappop(q)
        if vt > distance[vx][k]:
            continue
        for nx, dt in graph[vx]:
            nt = vt + dt
            if distance[nx][k] > nt:
                distance[nx][k] = nt
                distance[nx].sort()
                heapq.heappush(q,(nt,nx))

def print_answer(distance):
    for i in range(1,n+1):
        time = distance[i][k]
        if time >= INF:
            time = -1
        print(time)

if __name__ == "__main__":
    main()