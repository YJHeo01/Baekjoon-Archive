from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    depth = [-1] * (n+1)
    parent = [[0]*20 for _ in range(n+1)]
    max_size = [[0]*20 for _ in range(n+1)]
    min_size = [[int(1e9)]*20 for _ in range(n+1)]
    init(graph,depth,max_size,min_size,parent)
    k = int(input())
    for _ in range(k):
        query(depth,parent,max_size,min_size)

def init(graph,depth,max_size,min_size,parent):
    queue = deque([1])
    depth[1] = 0
    while queue:
        vx = queue.popleft()
        for nx, length in graph[vx]:
            if depth[nx] == -1:
                depth[nx] = depth[vx] + 1
                parent[nx][0] = vx
                max_size[nx][0], min_size[nx][0] = length, length
                queue.append(nx)
    
    for i in range(1,20):
        for j in range(1,n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
            max_size[j][i] = max(max_size[j][i-1],max_size[parent[j][i-1]][i-1])
            min_size[j][i] = min(min_size[j][i-1],min_size[parent[j][i-1]][i-1])

def query(depth,parent,max_size_list,min_size_list):
    max_value, min_value = 0,int(1e9)
    a,b = map(int,input().split())
    if depth[a] > depth[b]: a,b = b,a
    tmp = 1 << 19
    for i in range(19,-1,-1):
        if depth[b] - depth[a] >= tmp:
            max_value = max(max_value,max_size_list[b][i])
            min_value = min(min_value,min_size_list[b][i])
            b = parent[b][i]
        tmp >>= 1
    if a == b:
        print(min_value, max_value)
        return
    for i in range(19,-1,-1):
        if parent[a][i] != parent[b][i]:
            max_value = max(max_value,max_size_list[a][i],max_size_list[b][i])
            min_value = min(min_value,min_size_list[a][i],min_size_list[b][i])
            a = parent[a][i]
            b = parent[b][i]
    max_value = max(max_value,max_size_list[a][0],max_size_list[b][0])
    min_value = min(min_value,min_size_list[a][0],min_size_list[b][0])
    print(min_value,max_value)

if __name__ == "__main__":
    n = int(input())
    main()