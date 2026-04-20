def main():
    global n
    n = int(input())
    adj_graph = get_adj_graph(n)
    visited = [False] * n
    visited[0] = True
    adj_graph[0][0] = 0
    answer = dfs(adj_graph,visited,0,0)
    print(answer)

def get_adj_graph(n):
    graph = []
    for _ in range(n):
        tmp = list(input())
        for i in range(n): tmp[i] = int(tmp[i])
        graph.append(tmp)
    return graph

def dfs(graph,visited,last,cur):
    ret_value = 0
    cost = graph[last][cur]
    for next_node in range(n):
        if visited[next_node] == True or cost > graph[cur][next_node]:continue
        visited[next_node] = True
        ret_value = max(ret_value,dfs(graph,visited,cur,next_node))
        visited[next_node] = False
    ret_value += 1
    return ret_value

if __name__ == "__main__":
    main()