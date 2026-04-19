import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b); tree[b].append(a)

color = ['0'] + list(input().rstrip())

answer = 0

def dfs(tree,color,visited,vx):
    ret_value = 1
    for nx in tree[vx]:
        if visited[nx] or color[nx] == 'B': continue
        visited[nx] = True
        ret_value += dfs(tree,color,visited,nx)
        visited[nx] = False
    return ret_value

answer = 0

visited = [False] * (n+1)

for i in range(1,n+1):
    if color[i] == 'B':
        answer += dfs(tree,color,visited,i)
        answer -= 1

print(answer)