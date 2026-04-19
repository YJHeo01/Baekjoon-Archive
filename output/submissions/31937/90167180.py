import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

virus = [False] * (n+1)

tmp = list(map(int,input().split()))

for i in tmp:virus[i] = True

log = sorted([list(map(int,input().split())) for _ in range(m)])

for t,a,b in log:
    if virus[a] and virus[b]:
        print(a)
        break