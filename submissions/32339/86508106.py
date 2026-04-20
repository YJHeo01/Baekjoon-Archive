import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    p = list(map(int,input().split()))
    prior = [0] * 3
    for i in range(3):
        prior[p[i]] = i
    edges = []
    cnt = [0] * 3
    price = [0] * 3
    for _ in range(m):
        u,v,w,k = map(int,input().split())
        heapq.heappush(edges,(w,prior[k],u,v))
    parent = list(range(n+1))
    while edges:
        cost, rank, u, v= heapq.heappop(edges)
        if find_parent(parent,u) == find_parent(parent,v): continue
        union_parent(parent,u,v)
        idx = p[rank]
        cnt[idx] += 1
        price[idx] += cost
    print(sum(price))
    for i in range(3):
        print(cnt[i],price[i])
        

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

if __name__ == "__main__":
    main()