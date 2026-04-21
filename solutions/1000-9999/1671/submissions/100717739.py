import sys

input = sys.stdin.readline

n = int(input())

shark = []

for _ in range(n):
    shark.append(list(map(int,input().split())))
    
adj = [[] for _ in range(n)]

answer = n

for i in range(n):
    for j in range(n):
        if i == j: continue
        cnt = 0
        same = 0
        for k in range(3):
            if shark[i][k] >= shark[j][k]: cnt += 1
            if shark[i][k] == shark[j][k]: same += 1
        if same == 3 and i < j: continue
        if cnt == 3: adj[i].append(j)

A = [-1] * n
B = [-1] * n

def dfs(adj,A,B,a):
    visited[a] = True
    for b in adj[a]:
        if B[b] == -1 or (visited[B[b]] == False and dfs(adj,A,B,B[b])):
            A[a] = b
            B[b] = a
            return 1
    return 0

for _ in range(2):
    for i in range(n):
        visited = [False] * n
        answer -= dfs(adj,A,B,i)

print(answer)