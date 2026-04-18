import sys

input = sys.stdin.readline

n,m = map(int,input().split())

adj = [[] for _ in range(n)]

A = [-1] * n
B = [-1] * (m+1)

for i in range(n):
    tmp = list(map(int,input().split()))
    if tmp[0] == 0: continue
    for j in tmp[1:]:
        adj[i].append(j)


def dfs(adj,A,B,a):
    visited[a] = True
    for b in adj[a]:
        if B[b] == -1 or (visited[B[b]] == False and dfs(adj,A,B,B[b])):
            A[a] = b
            B[b] = a
            return 1
    return 0

answer = 0 

for i in range(n):
    if A[i] != -1: continue
    visited = [False] * n
    answer += dfs(adj,A,B,i)

print(answer)