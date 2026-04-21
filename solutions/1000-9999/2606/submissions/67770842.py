n = int(input())

pc = int(input())

array = [[] for _ in range(n+1)]

for i in range(pc):
    com1, com2  = map(int,input().split())
    array[com1].append(com2)

visited = [0]*(n+1)
answer = 0

def dfs(x):
    global visited
    global array
    global answer
    visited[x] = 1
    for i in array[x]:
        if visited[i] == 0:
            answer += 1
            dfs(i)
dfs(1)
print(answer)