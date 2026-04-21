import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def main():
    g = int(input())
    p = int(input())
    parent = [0] * (g+1)
    for i in range(g+1): parent[i] = i
    answer = 0
    for _ in range(p):
        n = int(input())
        tmp = find_parent(parent,n) 
        if tmp == 0:break
        answer += 1
        parent[tmp] -= 1
    print(answer)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

if __name__  == "__main__":
    main()