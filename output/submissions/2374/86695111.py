import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = [int(input()) for _ in range(n)]
    parent = list(range(n))
    answer = 0
    for i in range(1,n):
        a = find_parent(parent,i-1)
        b = find_parent(parent,i)
        if array[a] == array[b] and a != b:
            union_parent(parent,i-1,i)
    value_list = []
    for i in range(n):
        if find_parent(parent,i) == i:
            value_list.append((array[i]))
    value_list.sort()
    for i in range(1,n):
        answer += (value_list[i] - value_list[i-1])
    print(answer)
        
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

if __name__ == "__main__":
    main()