import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()
        
def solution():
    n = int(input())
    pos = []
    parent = list(range(n))
    for i in range(n):
        a_x, a_y, a_r = map(int,input().split())
        for j in range(i):
            b_x, b_y, b_r = pos[j]
            if (a_x-b_x) ** 2 + (a_y-b_y) ** 2 > (a_r+b_r) ** 2: continue
            union_parent(parent,i,j)
        pos.append((a_x,a_y,a_r))
    answer = 0
    for i in range(n):
        if find_parent(parent,i) == i: answer += 1
    print(answer)
        
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