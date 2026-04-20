import sys

sys.setrecursionlimit(2*10**5)

input = sys.stdin.readline

n,m = map(int,input().split())

high = [0] + list(map(int,input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    if high[a] > high[b]: graph[b].append(a)
    if high[b] > high[a]: graph[a].append(b)
    
def dfs(graph,max_cnt,x):
    for nx in graph[x]:
        if max_cnt[nx] != 0:
            max_cnt[x] = max(max_cnt[x],max_cnt[nx])
        else:
            max_cnt[x] = max(max_cnt[x],dfs(graph,max_cnt,nx))
    max_cnt[x] += 1
    return max_cnt[x]

max_cnt = [0] * (n+1)

for i in range(1,n+1):
    if max_cnt[i] == 0:
        dfs(graph,max_cnt,i)
    print(max_cnt[i])