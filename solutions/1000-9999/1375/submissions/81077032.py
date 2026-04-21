from collections import deque
import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    idx = 0
    human = {}
    younger_graph = [[] for _ in range(n)]
    parent = [0] * n
    for i in range(n): parent[i] = i
    for _ in range(m):
        a,b = input().rstrip().split()
        if a not in human:
            human[a] = idx
            idx += 1
        if b not in human:
            human[b] = idx
            idx += 1
        a_idx, b_idx = human[a], human[b]
        younger_graph[a_idx].append(b_idx)
        union_parent(parent,a_idx,b_idx)
    q = int(input())
    for _ in range(q):
        a,b = input().rstrip().split()
        if a not in human or b not in human or find_parent(parent,human[a]) != find_parent(parent,human[b]):
            print('gg',end=" ")
            continue
        visited = [False] * idx
        bfs(younger_graph,visited,human[a])
        bfs(younger_graph,visited,human[b])
        if visited[human[b]] == True: print(a,end=" ")
        elif visited[human[a]] == True: print(b,end=" ")
        else: print("gg",end=" ")

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def bfs(graph,visited,start):
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == False:
                visited[nx] = True
                queue.append(nx)

if __name__ == "__main__":
    main()