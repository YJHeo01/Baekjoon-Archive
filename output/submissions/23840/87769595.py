from itertools import permutations
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
    y = list(map(int,input().split()))
    node_list = [x] + y + [z]
    distance = []
    for i in range(p+2):
        tmp = [INF] * (n+1)
        solution(graph,tmp,node_list[i])
        distance.append(tmp)
    data = range(1,p+1)
    test_cast_list = list(permutations(data,p))
    answer = INF
    for test_case in test_cast_list:
        order = [0] + list(test_case) + [p+1]
        tmp = 0
        for i in range(p+1):
            vx = order[i]
            nx = node_list[order[i+1]]
            tmp += distance[vx][nx]
        answer = min(answer,tmp)
    if answer >= INF: answer = -1
    print(answer)

def solution(graph,distance,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, dd in graph[vx]:
            nd = dist + dd
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

if __name__ == "__main__":
    INF = int(1e30)
    main()