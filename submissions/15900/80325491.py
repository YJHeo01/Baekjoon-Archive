from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    if solution(get_graph(n),[-1] * (n+1)) % 2 == 1:print('Yes')
    else:print("No")

def get_graph(n):
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def solution(graph,visited):
    queue = deque([1])
    visited[1] = 0
    ret_value = 0
    while queue:
        vx = queue.popleft()
        leaf_node = True
        for nx in graph[vx]:
            if visited[nx] == -1:
                leaf_node = False
                visited[nx] = visited[vx] + 1
                queue.append(nx)
        if leaf_node == True:
            ret_value += visited[vx]
    return ret_value

if __name__ == "__main__":
    main()