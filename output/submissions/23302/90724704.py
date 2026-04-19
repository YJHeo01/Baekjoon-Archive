import sys

sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline

r,c = map(int,input().split())

sheet = [list(input().split()) for _ in range(r)]

graph = dict()

visited = dict()

for i in range(r):
    for j in range(c):
        if sheet[i][j] == '.': continue
        idx = chr(ord('A') + j % 26) + str(i+1)
        if j > ord('A'): idx = chr(ord('A')+1+j//26)
        tmp = sheet[i][j].split('+')
        if idx not in visited:
            visited[idx] = False
        if idx not in graph:
            graph[idx] = []
        for x in tmp:
            if x not in visited:
                visited[x] = False
                graph[x] = [idx]
            else:
                graph[x].append(idx)

not_cycle = set()

def dfs(graph,visited,x,not_cycle):
    for nx in graph[x]:
        if nx in not_cycle: continue
        if visited[nx]:
            print("yes")
            exit(0)
        visited[nx] = True
        dfs(graph,visited,nx,not_cycle)
    not_cycle.add(x)

for start in visited:
    if visited[start]: continue
    visited[start] = True
    dfs(graph,visited,start,not_cycle)
    
print("no")