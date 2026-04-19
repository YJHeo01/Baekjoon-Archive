from collections import deque
import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    graph, reverse_graph = get_graph()
    distance = [INF] * n
    get_shortest_path(graph,distance,s)
    shortest_path_edge = get_shortest_path_edge(reverse_graph,distance)
    distance = [INF] * n
    solution(graph,distance,shortest_path_edge)
    answer = distance[d]
    if answer >= INF:
        answer = -1
    print(answer)

def get_graph():
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v,p = map(int,input().split())
        graph[u].append((v,p))
        reverse_graph[v].append((u,p))
    return graph,reverse_graph

def get_shortest_path(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))

def get_shortest_path_edge(graph,distance):
    queue = deque([d])
    shortest_path_edge = [[False]*n for _ in range(n)]
    while queue:
        vx = queue.popleft()
        for nx, length in graph[vx]:
            if shortest_path_edge[nx][vx] == True:
                continue
            if distance[vx] == distance[nx] + length:
                shortest_path_edge[nx][vx] = True
                queue.append(nx)
    return shortest_path_edge

def solution(graph,distance,shortest_path_edge):
    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if shortest_path_edge[vx][nx] == True:
                continue
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))

if __name__ == "__main__":
    while True:
        n,m = map(int,input().split())
        if n == 0:
            break
        s,d = map(int,input().split())
        main()