from collections import deque
import sys

input = sys.stdin.readline

def main():
    power = [0] + [int(input()) for _ in range(n)]
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    distance = [INF] * (n+1)
    parent = [[0]*(n+1) for _ in range(20)]
    init(graph,distance,parent)
    
    for i in range(1,n+1):
        answer = i
        for j in range(19,-1,-1):
            if parent[j][answer] == 0: continue
            if power[i] >= distance[i] - distance[parent[j][answer]]:
                answer = parent[j][answer]
        print(answer)

def init(graph,distance,parent):
    queue = deque([1])
    distance[1] = 0
    while queue:
        vx = queue.popleft()
        for nx, dd in graph[vx]:
            if distance[nx] == INF:
                parent[0][nx] = vx
                distance[nx] = distance[vx] + dd
                queue.append(nx)
    for i in range(1,20):
        for j in range(1,n+1):
            parent[i][j] = parent[i-1][parent[i-1][j]]
    
if __name__ == "__main__":
    INF = int(1e14)
    n = int(input())
    main()