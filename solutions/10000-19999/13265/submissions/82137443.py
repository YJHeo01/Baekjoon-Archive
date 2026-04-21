import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        global n
        n,m = map(int,input().split())
        graph = get_graph(n,m)
        color = [0] * (n+1)
        print(solution(graph,color))

def get_graph(n,m):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    return graph

def solution(graph,color):
    for i in range(1,n+1):
        if color[i] == 0:
            color[i] = 1
            if dfs(graph,color,i) == 0:
                return "impossible"
    return "possible"

def dfs(graph,color,vx):
    ret_value = 1
    for nx in graph[vx]:
        if color[nx] == color[vx]:
            return 0
        if color[nx] == 0:
            if color[vx] == 1:
                color[nx] = 2
            else:
                color[nx] = 1
            ret_value = min(dfs(graph,color,nx),ret_value)
    return ret_value

if __name__ == "__main__":
    main()