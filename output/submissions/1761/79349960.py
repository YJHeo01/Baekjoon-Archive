from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b,length = map(int,input().split())
        graph[a].append((b,length))
        graph[b].append((a,length))
    layer = [-1] * (n+1)
    bfs(graph,layer)
    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        answer = 0
        if layer[a] > layer[b]: a,b = b,a
        while True:
            for nb, length in graph[b]:
                if layer[nb] == layer[b] - 1:
                    answer += length
                    b = nb
                    break
            if layer[b] == layer[a]:break
        while True:
            for na,length in graph[a]:
                if layer[na] == layer[a] - 1:
                    answer += length
                    a = na
                    break
            for nb, length in graph[b]:
                if layer[nb] == layer[b] - 1:
                    answer += length
                    b = nb
                    break
            if a == b: break
        print(answer)

def bfs(graph,layer):
    queue = deque([1])
    layer[1] = 0
    while queue:
        vx = queue.popleft()
        for nx, length in graph[vx]:
            if layer[nx] != -1:continue
            layer[nx] = layer[vx] + 1
            queue.append(nx)

if __name__ == "__main__":
    INF = int(1e9)
    main()