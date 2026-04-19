import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    parent = list(range(n+1))
    people = [0] + [int(input()) for _ in range(n)]
    for _ in range(m):
        o,p,q = map(int,input().split())
        if o == 1:
            alliance(parent,people,p,q)
        else:
            war(parent,people,p,q)
    visited = [False] * (n+1)
    answer = []
    for i in range(1,n+1):
        parent_idx = find_parent(parent,i)
        if visited[parent_idx] == False and people[parent_idx] > 0:
            answer.append(people[parent_idx])
            visited[parent_idx] = True
    print(len(answer))
    print(*sorted(answer))

def alliance(parent,people,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    union_parent(parent,a,b)
    people[a] += people[b]
    people[b] += people[a]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def war(parent,people,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    union_parent(parent,a,b)
    people[a] = abs(people[a]-people[b])
    people[b] = people[a]

if __name__ == "__main__":
    main()