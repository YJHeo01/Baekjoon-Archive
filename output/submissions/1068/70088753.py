def dfs(graph,start,remove):
    ret_v = 0
    if start == remove:
        return 0
    if graph[start] == []:
        return 1
    for point in graph[start]:
        ret_v += dfs(graph,point,remove)
    return ret_v


n = int(input())

nodes = list(map(int,input().split()))

remove_node_num = int(input())

tree = [[] for _ in range(n)]

for i in range(n):
    if nodes[i] == -1:
        parent_node = i
    else:
        tree[nodes[i]].append(i)

answer = dfs(tree,parent_node,remove_node_num)

print(answer)