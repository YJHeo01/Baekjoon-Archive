from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    graph = get_graph(n)
    parent = [0] * (n+1)
    depth = [-1] * (n+1)
    array = list(map(int,input().split()))
    if array[0] != 1:
        print(0)
        return
    answer = 1
    init_parent_depth(graph,parent,depth)
    for i in range(1,n):
        if depth[array[i]] > depth[array[i-1]] and parent[array[i]] != array[i-1]:
            answer = 0
            break
        if depth[array[i]] == depth[array[i-1]] and parent[array[i]] != parent[array[i-1]]:
            answer = 0
            break
    print(answer)


def get_graph(n):
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def init_parent_depth(graph,parent,depth):
    queue = deque([1])
    depth[1] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if depth[nx] == -1:
                depth[nx] = depth[vx] + 1
                parent[nx] = vx
                queue.append(nx)


if __name__ == "__main__":
    main()