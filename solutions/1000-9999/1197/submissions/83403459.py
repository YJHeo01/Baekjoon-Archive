import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def main():
    v, e = map(int,input().split())
    edges = []
    parent = list(range(v+1))
    for _ in range(e):
        a,b,c = map(int,input().split())
        edges.append((c,a,b))
    edges.sort()
    answer = 0
    for c,a,b in edges:
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            answer += c
    print(answer)

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

if __name__ == "__main__":
    main()