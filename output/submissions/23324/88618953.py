import sys

input = sys.stdin.readline

def main():
    
    n,m,k = map(int,input().split())

    edges = []

    for _ in range(k): edges.append(list(map(int,input().split())))
    
    global root_a, root_b
    root_a, root_b = map(int,input().split())

    for i in range(k+1,m): edges.append(list(map(int,input().split())))
    
    parent = list(range(n+1))
    
    for u,v in edges:
        union_parent(parent,u,v)
    
    tmp_a, tmp_b = 0,0
    
    for i in range(1,n+1):
        if find_parent(parent,i) == root_a: tmp_a += 1
        else: tmp_b += 1
    
    answer = tmp_a * tmp_b
    
    print(answer)

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a == root_a or a == root_b:
        parent[b] = a
    else:
        parent[a] = b
    
def find_parent(parent,x):
    if parent[x] != x: parent[x] = find_parent(parent,parent[x])
    return parent[x]

if __name__ == "__main__":
    main()