from collections import deque
import sys, heapq

input = sys.stdin.readline

def main():
    graph = [[] for _ in range(n+1)]
    p,q = map(int,input().split())
    zb = [int(input()) for _ in range(k)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b); graph[b].append(a)
    danger_zone = bfs(graph,[-1]*(n+1),zb)
    distance = [INF] * (n+1)
    print(dijkstra(graph,distance,danger_zone,q,p))

def bfs(graph,visited,start):
    queue = deque(start)
    for i in start: visited[i] = 0
    while queue:
        vx = queue.popleft()
        if visited[vx] == s: break
        for nx in graph[vx]:
            if visited[nx] == -1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
    return visited

def dijkstra(graph,distance,danger_zone,expensive_cost,normal_cost):
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    ret_value = INF
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx in graph[vx]:
            if nx == n:
                ret_value = min(ret_value,dist)
                continue
            if danger_zone[nx] == 0: continue
            if danger_zone[nx] == -1: next_dist = dist + normal_cost
            else: next_dist = dist + expensive_cost
            if distance[nx] > next_dist:
                distance[nx] = next_dist
                heapq.heappush(q,(next_dist,nx))
    return ret_value

if __name__ == "__main__":
    n,m,k,s = map(int,input().split())
    INF = int(1e12)
    main()