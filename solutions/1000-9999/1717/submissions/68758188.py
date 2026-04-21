import sys
input = sys.stdin.readline
n, m = map(int,input().split())

n_set = [0] * (n+1)
def find_parent(parent,x):
    if x != parent[x]:
        return find_parent(parent,parent[x])
    return parent[x]

def union_set(parent,a,b):
    a_ = find_parent(parent,a)
    b_ = find_parent(parent,b)
    if a_ < b_:
        n_set[b] = a_
    elif a_ > b_:
        n_set[a] = b_
    else:
        return

for i in range(0,n+1):
    n_set[i] = i

for i in range(m):
    c,a,b = map(int,input().split())
    if c == 0:
        union_set(n_set,a,b)
    if c==1:
        if n_set[a] == n_set[b]:
            print("YES")
        else:
            print("NO")
