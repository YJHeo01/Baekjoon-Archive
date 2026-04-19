import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

virus = [False] * (n+1)

tmp = list(map(int,input().split()))

for i in tmp:virus[i] = True

log = sorted([list(map(int,input().split())) for _ in range(m)])

for i in range(1,n+1):
    visited = [False] * (n+1)
    visited[i] = True
    for t,a,b in log:
        if visited[a]: visited[b] = True
    finish = True
    for j in range(1,n+1):
        if visited[j] != virus[j]: finish = False
    if finish:
        print(i)
        break