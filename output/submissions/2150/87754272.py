import sys

sys.setrecursionlimit(int(1e6)+7)
input = sys.stdin.readline

def main():
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
    for i in range(1,v+1):
        graph[i].sort()
    parent = [0] * (v+1)
    scc = [[] for _ in range(v+1)]
    finish = [False] * (v+1)
    for i in range(1,v+1):
        if parent[i] != 0: continue
        dfs(graph,parent,i,scc,finish)
    cnt = 0
    answer = [[] for _ in range(v+1)]
    
    for i in range(1,v+1):
        if scc[i] == []: continue
        scc[i].sort()
        answer[scc[i][0]] = scc[i]
    for i in range(1,v+1):
        if answer[i] != []: cnt += 1
    print(cnt)
    scc.sort()
    for i in range(1,v+1):
        if answer[i] == []: continue
        print(*answer[i],end=" ")
        print(-1)

def dfs(graph,parent,vx,scc,finish):
    parent[vx] = vx
    for nx in graph[vx]:
        if finish[nx]: continue
        if parent[nx] == 0:
            dfs(graph,parent,nx,scc,finish)
            if parent[nx] != nx:
                parent[vx] = parent[nx]
        else:
            parent[vx] = parent[nx]
    finish[vx] = True
    scc[parent[vx]].append(vx)

if __name__ == "__main__":
    main()