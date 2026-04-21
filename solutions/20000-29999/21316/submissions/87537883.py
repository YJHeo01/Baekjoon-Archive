from collections import deque
import sys

input = sys.stdin.readline

def main():
    adj_graph = [[] for _ in range(13)]
    edge_cnt = [0] * 13
    for _ in range(12):
        x,y = map(int,input().split())
        edge_cnt[x] += 1; edge_cnt[y] += 1
        adj_graph[x].append(y); adj_graph[y].append(x)
    leaf_node = []
    depth = [-1] * 13
    for i in range(13):
        if edge_cnt[i] == 1:
            leaf_node.append(i)
            depth[i] = 0
    queue = deque(leaf_node)
    while queue:
        vx = queue.popleft()
        for nx in adj_graph[vx]:
            if depth[nx] == -1:
                depth[nx] = depth[vx] + 1
                queue.append(nx)
    for i in range(13):
        if edge_cnt[i] != 3 or depth[i] != 1: continue
        visited = [False] * 4
        state = 3
        for j in adj_graph[i]:
            if visited[edge_cnt[j]] == False:
                visited[edge_cnt[j]] = True
                state -= 1
        if state == 0:
            print(i)
            break


if __name__ == "__main__":
    main()