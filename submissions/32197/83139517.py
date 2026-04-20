import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e,t = map(int,input().split())
        graph[s].append((e,t))
        graph[e].append((s,t))
    a,b = map(int,input().split())
    INF = int(1e9)
    distance = [[INF] * 2 for _ in range(n+1)]
    solution(graph,distance,a)
    print(min(distance[b]))

def solution(graph,distance,start):
    q = []
    distance[start][0], distance[start][1] = 0,0
    heapq.heappush(q,(0,0,start))
    heapq.heappush(q,(0,1,start))
    while q:
        dist, state, vx = heapq.heappop(q)
        if dist > distance[vx][state]:
            continue
        for nx, next_state in graph[vx]:
            nd = distance[vx][state]
            if state != next_state: nd += 1
            if distance[nx][next_state] > nd:
                distance[nx][next_state] = nd
                heapq.heappush(q,(nd,next_state,nx))

if __name__ == "__main__":
    main()