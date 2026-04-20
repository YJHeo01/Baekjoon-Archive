import sys

input = sys.stdin.readline

def main():
    graph = [[] for _ in range(v+1)]
    edges = get_edges(graph)
    visited = [False] * e
    yes = dfs(graph,edges,visited,1,0)
    if yes == True: print('YES')
    else:print('NO')

def get_edges(graph):
    edges = []
    for edge_idx in range(e):
        a,b = map(int,input().split())
        edges.append([a,b])
        graph[a].append(edge_idx)
        graph[b].append(edge_idx)
    return edges

def dfs(graph,edges,visited,start,cnt):
    if cnt == e: return True
    ret_value = False
    for edge_idx in graph[start]:
        if visited[edge_idx] == True: continue
        visited[edge_idx] = True
        nx = search_nx(edges[edge_idx],start)
        ret_value = ret_value or dfs(graph,edges,visited,nx,cnt+1)
        visited[edge_idx] = False
    return ret_value 
        
def search_nx(edge,start):
    for idx in edge:
        if idx != start: return idx

if __name__ == "__main__":
    v,e = map(int,input().split())
    main()