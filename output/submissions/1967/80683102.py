import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    global answer
    answer = 0
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c = map(int,input().split())
        tree[a].append((b,c))
    dfs(tree,0,1)
    print(answer)

def dfs(graph,value,vx):
    global answer
    if graph[vx] == []:
        return value
    leaf_node_distance = []
    for nx,nd in graph[vx]:
        leaf_node_distance.append(dfs(graph,value+nd,nx))
    leaf_node_distance.sort()
    if len(leaf_node_distance) >= 2:
        answer = max(answer,leaf_node_distance[0]+leaf_node_distance[1])
    else:
        answer = max(answer,leaf_node_distance[0])
    return leaf_node_distance[0]
    
if __name__ == "__main__":
    main()
