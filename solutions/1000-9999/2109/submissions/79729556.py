import sys,heapq

input = sys.stdin.readline

def main():
    n = int(input())
    q = []
    for _ in range(n):
        a,b = map(int,input().split())
        heapq.heappush(q,(-a,b))
    parent = [0] * 10001
    for i in range(10001): parent[i] = i
    answer = 0
    while q:
        a,b = heapq.heappop(q)
        p_idx = find_parent(parent,b)
        if p_idx != 0:
            parent[p_idx] -= 1
            answer -= a
    print(answer)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,x-1)
    return parent[x]

if __name__  == "__main__":
    main()