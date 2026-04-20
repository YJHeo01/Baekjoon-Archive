import sys

input = sys.stdin.readline

n = int(input())

parent = [0] * (n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    if a == 1:
        parent[b] = a
    elif b == 1:
        parent[a] = b
    else:
        if parent[a] == 0:
            parent[a] = b
        else:
            parent[b] = a

for i in range(2,n+1):
    print(parent[i])