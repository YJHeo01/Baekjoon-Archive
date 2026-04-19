import sys

sys.setrecursionlimit(int(1e6)+7)
input = sys.stdin.readline
id = 0
def main():
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
    for i in range(1,v+1):
        graph[i].sort()
    parent = [0] * (v+1)
    scc = []
    finish = [False] * (v+1)
    stack = []
    for i in range(1,v+1):
        if finish[i]: continue
        dfs(graph,parent,i,scc,finish,stack)
    scc.sort()
    print(len(scc))
    for s in scc:
        print(*s,end=" ")
        print(-1)

def dfs(graph,depth,vx,scc,finish,stack):
    global id
    id += 1
    root = id
    depth[vx] = id
    stack.append(vx)
    for nx in graph[vx]:
        if finish[nx]: continue
        if depth[nx] == 0:
            root = min(root,dfs(graph,depth,nx,scc,finish,stack))
        else:
            root = min(root,depth[nx])
    if root == depth[vx]:
        tmp = []
        while True:
            x = stack.pop()
            tmp.append(x)
            finish[x] = True
            if x == vx: break
        tmp.sort()
        scc.append(tmp)
    return root
            

if __name__ == "__main__":
    main()