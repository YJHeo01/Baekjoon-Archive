import sys

input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

try:
    while True:
        n,m = map(int,input().split())
        parent = list(range(n+1))
        for _ in range(m):
            a,b = map(int,input().split())
            union_parent(parent,a,b)
        cnt = [0] * (n+1)
        for i in range(1,n+1):
            cnt[find_parent(parent,i)] += 1
        answer = "NO"
        for i in range(n+1):
            if cnt[i] >= 5: answer = "YES"
        print(answer)
        
except:
    exit()