import sys

input = sys.stdin.readline

def main():
    idx = 1
    while True:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            return
        print("Case " + str(idx)+":",end=" ")
        t = solution(n,m)
        if t == 0:
            print("No trees.")
        elif t == 1:
            print("There is one tree.")
        else:
            print("A forest of " +str(t)+ " trees.")
        idx += 1

def solution(n,m):
    cycle = [False] * (n+1)
    tree = [False] * (n+1)
    parent = list(range(n+1))
    
    for _ in range(m):
        a,b = map(int,input().split())
        if find_parent(parent,a) == find_parent(parent,b):
            cycle[a], cycle[b] = True, True
        else:
            union_parent(parent,a,b)
    
    for i in range(1,n+1):
        if cycle[i] == False:
            continue
        cycle[find_parent(parent,i)] = True

    cnt = 0
    for i in range(1,n+1):
        parent_node = find_parent(parent,i)
        if cycle[parent_node] == True or tree[parent_node] == True:
            continue
        cnt += 1
        tree[parent_node] = True
    return cnt

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