import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

parent = [0] * (n+1)

def find_parent(start):
    node_queue = deque([start])
    while node_queue:
        node = node_queue.popleft()
        for i in tree[node]:
            if parent[i] == 0:
                parent[i] = node
                node_queue.append(i)
            

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

find_parent(1)

for i in range(2,n+1):
    print(parent[i])