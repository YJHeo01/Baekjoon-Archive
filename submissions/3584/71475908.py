#https://github.com/YJHeo01
from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

def find_LCA(graph,visited,node1,node2):
    queue = deque([node1,node2])
    visited[node1] = True
    visited[node2] = True
    while queue:
        node = queue.popleft()
        parent_node = graph[node]
        if visited[parent_node] == True:
            return parent_node
        visited[parent_node] = True
        queue.append(parent_node)

for _ in range(t):
    n = int(input())
    graph = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[b] = a
    node1, node2 = map(int,input().split())
    visited = [False] * (n+1)
    print(find_LCA(graph,visited,node1,node2))