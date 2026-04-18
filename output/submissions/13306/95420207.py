import sys

sys.setrecursionlimit(200010)

input = sys.stdin.readline

n,q = map(int,input().split())

parent = [0,0]

for i in range(n-1):
    a = int(input())
    parent.append(a)
    
stack = [list(map(int,input().split())) for _ in range(n+q-1)]

s = list(range(n+1))

def find_parent(s,x):
    if s[x] != x:
        s[x] = find_parent(s,s[x])
    return s[x]

def union_parent(s,a,b):
    a = find_parent(s,a)
    b = find_parent(s,b)
    s[b] = s[a]

answer = []

while stack:
    tmp = stack.pop()
    if tmp[0] == 0:
        b = tmp[1]
        union_parent(s,parent[b],b)
    else:
        c,d = tmp[1], tmp[2]
        if find_parent(s,c) == find_parent(s,d):
            answer.append("YES")
        else:
            answer.append("NO")

while answer:
    print(answer.pop())