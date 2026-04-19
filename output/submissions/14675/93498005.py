import sys

input = sys.stdin.readline

n = int(input())

cnt = [0] * (n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    cnt[a] += 1
    cnt[b] += 1

q = int(input())

for _ in range(q):
    t,k = map(int,input().split())
    if t == 1:
        if cnt[k] == 1: print("no")
        else: print("yes")
    else:
        print("yes")