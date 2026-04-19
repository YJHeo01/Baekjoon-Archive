import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()

def solution():
    f = int(input())
    id_inf = 0
    id_list = dict()
    cnt = []
    parent = []
    for _ in range(f):
        name_a, name_b = input().split()
        if name_a not in id_list:
            id_list[name_a] = id_inf
            parent.append(id_inf)
            id_inf += 1
            cnt.append(1)
        if name_b not in id_list:
            id_list[name_b] = id_inf
            parent.append(id_inf)
            id_inf += 1
            cnt.append(1)
        id_a, id_b = id_list[name_a], id_list[name_b]
        if find_parent(parent,id_a) != find_parent(parent,id_b):
            union(parent,cnt,id_a,id_b)
        print(cnt[find_parent(parent,id_a)])
            
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,cnt,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        cnt[a] += cnt[b]
        parent[b] = a
    else:
        cnt[b] += cnt[a]
        parent[a] = b


if __name__ == "__main__":
    main()