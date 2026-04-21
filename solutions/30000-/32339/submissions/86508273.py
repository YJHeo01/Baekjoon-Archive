import sys, heapq

sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    p = list(map(int,input().split()))
    prior = [0] * 3
    for i in range(3):
        prior[p[i]] = i
    edges = []
    cntOfRoad = [0] * 3
    priceOfRoad = [0] * 3
    for _ in range(m):
        u,v,w,k = map(int,input().split())
        heapq.heappush(edges,(w,prior[k],u,v))
    parent = list(range(n+1))
    while edges:
        cost, rank, u, v= heapq.heappop(edges)
        if check_same_parent(parent,u,v): continue
        idx = p[rank]
        cntOfRoad[idx] += 1
        priceOfRoad[idx] += cost
    print(sum(priceOfRoad))
    for i in range(3):
        print(cntOfRoad[i],priceOfRoad[i])

def check_same_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a == b: return True
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return False

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

if __name__ == "__main__":
    main()