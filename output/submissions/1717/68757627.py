import sys
input = sys.stdin.readline
n, m = map(int,input().split())

n_set = [0] * (n+1)
def find_parent(parent,x):
    if x != parent[x]:
        return find_parent(parent,parent[x])
    return parent[x]

def union_set(a,b):
    a = find_parent(n_set,a)
    b = find_parent(n_set,a)
    if a < b:
        n_set[b] = a
    elif a > b:
        n_set[a] = b
    else:
        return

for i in range(0,n+1):
    n_set[i] = i

for i in range(m):
    c,a,b = map(int,input().split())
    if c == 0:
        union_set(a,b)
    if c==1:
        if n_set[a] == n_set[b]:
            print("YES")
        else:
            print("NO")