n = int(input())

pc = int(input())

array = [[] for _ in range(n+1)]

for i in range(pc):
    com1, com2  = map(int,input().split())
    array[com1].append(com2)
    array[com2].append(com1)

visited = [0]*(n+1)
answer = 0

def dfs(graph,visited,x):
    global answer
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            answer += 1
            dfs(graph,visited,i)
    
dfs(array,visited,1)
print(answer)