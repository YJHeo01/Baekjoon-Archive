import sys

input = sys.stdin.readline

test_case_idx = 0

def check_tree(graph,visited,cur_node):
    ret_value = True
    for next_node in graph[cur_node]:
        if visited[next_node] == -1:
            visited[next_node] -= 1
        elif visited[next_node] == -2:
            return False
        elif visited[next_node] == 0:
            visited[next_node] = 1
            ret_value = ret_value and check_tree(graph,visited,next_node)
        else:
            continue
    return ret_value

while True:
    n,m = map(int,input().split())
    if n == 0:
        break
    tree_cnt = 0
    test_case_idx += 1
    graph = [[] for _ in range(n+1)]
    edge_cnt = [0] * (n+1)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        edge_cnt[a] += 1
        edge_cnt[b] += 1
    visited = [0] * (n+1)
    for i in range(1,n+1):
        if visited[i] == 0 and edge_cnt[i] <= 1:
            visited[i] = -1
            if check_tree(graph,visited,i) == True:
                tree_cnt += 1
    print("Case " + str(test_case_idx) + ": ",end="")
    if tree_cnt == 0:
        print("No trees.")
    elif tree_cnt == 1:
        print("There is one tree.")
    else:
        print("A forest of " + str(tree_cnt) + " trees.")