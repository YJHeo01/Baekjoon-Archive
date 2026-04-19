import sys
from collections import deque

input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        degree[a] += 1; degree[b] += 1
        graph[a].append(b); graph[b].append(a)
    root = []
    for vx in range(1,n+1):
        if degree[vx] == 1: continue
        if degree[vx] != 3:
            print(-1)
            return
        if possible_root(graph,degree,[-1]*(n+1),vx) == True: root.append(vx)
    if root == []:
        print(-1)
    else:
        print(len(root))
        for i in root:
            print(i,end=" ")

def possible_root(graph,degree,distance,start):
    queue = deque([start])
    last_distance = -1
    distance[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if distance[nx] == -1:
                distance[nx] = distance[vx] + 1
                if degree[nx] == 1:
                    if last_distance == -1: last_distance = distance[nx]
                    if last_distance != distance[nx]: return False
                queue.append(nx)
    return True

if __name__ == "__main__":
    main()