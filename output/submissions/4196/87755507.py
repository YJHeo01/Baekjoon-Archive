from collections import deque
import sys

sys.setrecursionlimit(int(1e5)+7)
input = sys.stdin.readline
id = 0

def main():
    for _ in range(int(input())):
        soluton()
def soluton():
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    indegree = [0] * (v+1)
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1
    q = deque([])
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    parent = [0] * (v+1)
    finish = [False] * (v+1)
    stack = []
    answer = 0
    while q:
        vx = q.popleft()
        if finish[vx]: continue
        answer += 1
        dfs(graph,parent,vx,finish,stack)
    print(max(1,answer))
def dfs(graph,parent,vx,finish,stack):
    global id
    id += 1
    root = id
    parent[vx] = id
    stack.append(vx)
    for nx in graph[vx]:
        if finish[nx]: continue
        if parent[nx] == 0:
            root = min(root,dfs(graph,parent,nx,finish,stack))
        else:
            root = min(root,parent[nx])
    if root == parent[vx]:
        while True:
            x = stack.pop()
            finish[x] = True
            if x == vx: break
    return root
            
if __name__ == "__main__":
    main()