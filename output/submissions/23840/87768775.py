import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    x,z = map(int,input().split())
    p = int(input())
    bitmask = 1 << p
    mid_idx = [-1] * (n+1)
    y = list(map(int,input().split()))
    for i in range(p):
        mid_idx[y[i]] = i
    distance = [[INF]*bitmask for _ in range(n+1)]
    solution(graph,distance,x,mid_idx)
    answer = distance[z][bitmask-1]
    if answer >= INF: answer = -1
    print(answer)

def solution(graph,distance,start,mid):
    q = []
    distance[start][0] = 0
    heapq.heappush(q,(0,0,start))
    while q:
        dist, state, vx = heapq.heappop(q)
        if dist > distance[vx][state]: continue
        for nx, dd in graph[vx]:
            next_state = state
            if mid[nx] != -1:
                next_state |= 1 << mid[nx]
            nd = dist + dd
            if distance[nx][next_state] > nd:
                distance[nx][next_state] = nd
                heapq.heappush(q,(nd,next_state,nx))

if __name__ == "__main__":
    INF = int(1e30)
    main()