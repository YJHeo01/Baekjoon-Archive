import sys

input = sys.stdin.readline

t = int(input())

def solution():
    n = int(input())
    array = [0] + list(map(int,input().split()))
    parent = list(range(n+1))
    answer = 0
    for i in range(1,n+1):
        if array[i] == i: answer += 1; continue
        parent[find_parent(parent,i)] = parent[find_parent(parent,array[i])]
    target = [False] * (n+1)
    for i in range(1,n+1):
        if array[i] == i: continue
        if find_parent(parent,i) == i: target[i] = True
    for i in range(1,n+1):
        if target[find_parent(parent,i)]: answer += 1
    answer = n - answer
    print(answer)
    
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

for _ in range(t):
    solution()