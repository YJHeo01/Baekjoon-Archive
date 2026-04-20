import sys

sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
child_cnt = [1] * (n+1)
depth = [-1] * (n+1)
depth[0] = 0
depth[1] = 0

def dfs(graph,depth,child_cnt,x):
    for nx in graph[x]:
        if depth[nx] != -1: continue
        depth[nx] = depth[x] + 1
        child_cnt[x] += dfs(graph,depth,child_cnt,nx)
    return child_cnt[x]

dfs(tree,depth,child_cnt,1)

distance_sum = sum(depth) // 2

answer = 0

for i in range(1,n+1):
    answer -= (child_cnt[i]-1) * depth[i]
    answer += (n-child_cnt[i]) * depth[i]
    
answer += (n//2)

print(answer)