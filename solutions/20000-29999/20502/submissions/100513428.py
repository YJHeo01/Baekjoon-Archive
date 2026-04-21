import sys

input = sys.stdin.readline

n,m = map(int,input().split())

rank = list(map(int,input().split()))

arr = [[] for _ in range(m+1)]

for i in range(n):
    tmp = list(map(int,input().split()))
    for k in tmp[1:]:
        arr[k].append((rank[i],i+1))

for i in range(m+1): rank.sort()

q = int(input())

for _ in range(q):
    k = int(input())
    if arr[k] == []: print(-1)
    else:
        for answer in arr[k]:
            print(answer[1],end=" ")
        print()