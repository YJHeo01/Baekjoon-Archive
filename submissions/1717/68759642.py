import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m = map(int,input().split())

parent = [0] * (n+1)
def find_parent(x):
    if x != parent[x]:
        return find_parent(parent[x])
    return parent[x]

def union_set(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(0,n+1):
    parent[i] = i

for i in range(m):
    c,a,b = map(int,input().split())
    if c == 0:
        union_set(a,b)
    if c==1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")