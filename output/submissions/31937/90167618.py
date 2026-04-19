import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

if k == 1:
    print(int(input()))
    exit(0)

virus = [False] * (n+1)

tmp = list(map(int,input().split()))

for i in tmp:virus[i] = True

log = sorted([list(map(int,input().split())) for _ in range(m)])

def simulation(log,visited,start):
    for i in range(start+1,m):
        t,a,b = log[i]
        if visited[a]:
            visited[b] = True
            if virus[b] == False: return False
    return True

for i in range(m):
    if virus[log[i][1]] == False or virus[log[i][2]] == False: continue
    visited = [False] * (n+1)
    visited[log[i][1]], visited[log[i][2]] = True, True
    if simulation(log,[False]*(n+1),i):
        print(log[i][1])
        break