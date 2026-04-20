import sys

input = sys.stdin.readline

n = int(input())

tree = [0] * (n+1)

magic = [0] * (n+1)

tree_idx = 0

for _ in range(n):
    a,b = map(int,input().split())
    if a == 1:
        tree_idx += 1
        tree[tree_idx] = b
    else:
        magic[tree_idx] += b

answer = 0

tmp = -1

for i in range(n,0,-1):
    if magic[i] != 0:
        tmp = tree[i] - magic[i]
        if tmp < 0: break
    if tmp < 0: answer += tree[i]
    else: answer += tmp

print(answer)