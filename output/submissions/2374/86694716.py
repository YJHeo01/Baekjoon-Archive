import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = [int(input()) for _ in range(n)]
    parent = list(range(n+1))
    answer = 0
    for _ in range(n):
        value_list = []
        for i in range(1,n):
            if array[i-1] == array[i]:
                union_parent(parent,i-1,i)
        for i in range(n):
            if find_parent(parent,i) == i:
                value_list.append((array[i],i))
        if len(value_list) == 1: break
        value_list.sort()
        min_value,min_idx = value_list[0]
        second_value, second_idx = value_list[1]
        answer += (second_value-min_value)
        array[min_idx] = second_value
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