##LGCPC 예비소집 _lgcpc2024qual_00019

import sys

input = sys.stdin.readline

def main():
    n,m,k = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(m)]
    remove = [False] * m
    for i in range(k):
        answer = 0
        parent = list(range(n+1))
        edge_cnt = 0
        remove_idx = -1
        for j in range(m):
            if remove[j] == True: continue
            value = j + 1
            a,b = edges[j]
            if find_parent(parent,a) != find_parent(parent,b):
                union_parent(parent,a,b)
                answer += value
                edge_cnt += 1
                if remove_idx == -1: remove_idx = j
            if edge_cnt == n-1:
                break
        remove[remove_idx] = True
        if edge_cnt == n-1:
            print(answer,end=" ")
        else:
            print(0,end=" ")

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

if __name__ == "__main__":
    main()