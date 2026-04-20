from collections import deque
import sys

sys.setrecursionlimit(4*10**6)
input = sys.stdin.readline

def main():
    n,a,b = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v); graph[v].append(u)
    visited = [False] * (n+1)
    possible_root = [False] * (n+1)
    dfs(graph,visited,a,b,possible_root)
    dfs(graph,visited,b,a,possible_root)
    possible_root[a] = False; possible_root[b] = False
    #for i in range(1,n+1):
        #if possible_root[i] == True:
            #bfs(graph,possible_root,i,a,b)
    answer = 0
    for i in range(1,n+1):
        if possible_root[i]: answer += 1
    print(answer)


def dfs(graph,visited,vx,target,possible_root):
    if target == vx: return 1
    ret_value = 0
    for nx in graph[vx]:
        if visited[nx] == False:
            visited[nx] = True
            ret_value += dfs(graph,visited,nx,target,possible_root)
    if ret_value != 0:
        ret_value += 1
        possible_root[vx] = True
    return ret_value

def bfs(graph,visited,start,a,b):
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if nx == a or nx == b or visited[nx]: continue
            visited[nx] = True
            queue.append(nx)

if __name__ == "__main__":
    main()