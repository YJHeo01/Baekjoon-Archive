n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    
A = [-1] * (n+1)
B = [-1] * (n+1)

def dfs(visited,a):
    visited[a] = True
    for b in graph[a]:
        if B[b] == -1 or (visited[B[b]]==False and dfs(visited,B[b])):
            A[a] = b
            B[b] = a
            return True
    return False

answer = 0

for i in range(1,n+1):
    answer += dfs([False]*(n+1),i)

print(answer)