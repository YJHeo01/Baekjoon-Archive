import sys

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

parent = [0] * (n+1)

def find_parent(num):
    child_node = []
    for i in tree[num]:
        if parent[i] == 0:
            parent[i] = num
            child_node.append(i)
    for node in child_node:
        find_parent(node)
            

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

find_parent(1)

for i in range(2,n+1):
    print(parent[i])