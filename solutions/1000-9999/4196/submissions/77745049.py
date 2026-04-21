import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        global n
        n,m = map(int,input().split())
        indegree = [0] * (n+1)
        graph = get_graph_and_set_indegree(indegree,m)
        visited = [False] * (n+1); finish = True        
        target_indegree = 0; answer = 0
        while True:
            for i in range(1,n+1):
                if indegree[i] == target_indegree and visited[i] == False:
                    visited[i] = True; finish = False
                    answer += dfs(graph,visited,i)
            if finish == True:
                break
            finish = True
        print(answer)

def get_graph_and_set_indegree(indegree,m):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        set_indegree(indegree,b)
        graph[a].append(b)
    return graph
    
def set_indegree(indegree,b):
    indegree[b] += 1

def dfs(graph,visited,vx):
    for nx in graph[vx]:
        if visited[nx] == False:
            visited[nx] = True
            dfs(graph,visited,nx)
    return 1

if __name__ == "__main__":
    main()