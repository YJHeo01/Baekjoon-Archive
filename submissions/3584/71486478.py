#https://github.com/YJHeo01/BOJ/blob/main/%EA%B0%80%EC%9E%A5%20%EA%B0%80%EA%B9%8C%EC%9A%B4%20%EA%B3%B5%ED%86%B5%20%EC%A1%B0%EC%83%81%20-%203584%EB%B2%88.py

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def check_parent(graph,visited,start):
    if start == 0:
        return
    parent_node = graph[start]
    visited[start] = True
    check_parent(graph,visited,parent_node)

def find_LCA(graph,visited,start):
    if visited[start] == True:
        return start
    return find_LCA(graph,visited,graph[start])

for _ in range(t):
    n = int(input())
    parent = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        parent[b] = a
    node1, node2 = map(int,input().split())
    visited = [False] * (n+1)
    check_parent(parent,visited,node1)
    answer = find_LCA(parent,visited,node2)
    print(answer)