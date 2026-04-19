import sys

sys.setrecursionlimit(10**6+1)
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
    s = int(input())
    s = list(map(int,input().split()))
    fan = [False] * (n+1)
    for i in s:
        fan[i] = True
    dfs(graph,fan,1)
    print("Yes")
    
def dfs(graph,fanOrVisited,vx):
    if fanOrVisited[vx] == True: return
    fanOrVisited[vx] == True
    if graph[vx] == []:
        print("yes")
        exit(0)
    for nx in graph[vx]:
        if fanOrVisited[nx] == True: continue
        dfs(graph,fanOrVisited,nx)

if __name__ == "__main__":
    main()