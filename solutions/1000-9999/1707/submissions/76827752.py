import sys

input = sys.stdin.readline

k = int(input())

def solution(graph,visited_node,visited_edge,vx):
    ret_value = True
    visited_node[vx] = True
    for nx in graph[vx]:
        if visited_edge[vx][nx] == True:
            continue
        visited_edge[nx][vx] = True
        if visited_node[nx] == True:
            return False
        else:
            ret_value = ret_value and solution(graph,visited_node,visited_edge,nx)
    return ret_value

for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited_node = [False] * (v+1)
    visited_edge = [[False]*(v+1) for _ in range(v+1)]
    binary_graph = solution(graph,visited_node,visited_edge,1)
    if binary_graph == True:
        print("YES")
    else:
        print("NO")