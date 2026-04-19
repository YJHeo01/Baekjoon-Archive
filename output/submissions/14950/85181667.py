import sys, heapq

input = sys.stdin.readline

def main():
    n,m,t = map(int,input().split())
    parent = list(range(n+1))
    q = []
    cnt = 0
    answer = 0
    for _ in range(m):
        a,b,c = map(int,input().split())
        heapq.heappush(q,(c,a,b))
    while q:
        cost, a, b = heapq.heappop(q)
        if union_parent(parent,a,b):
            answer += cost
            answer += cnt * t
            cnt += 1
    print(answer)

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a == b: return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

if __name__ == "__main__":
    main()