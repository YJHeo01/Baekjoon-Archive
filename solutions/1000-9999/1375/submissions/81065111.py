from collections import deque
import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    idx = 0
    human = {}
    graph = [[] for _ in range(n+1)]
    parent = [0] * n
    depth = [-1] * n 
    oldest = [True] * n
    for _ in range(m):
        a,b = input().rstrip().split()
        if a not in human:
            human[a] = idx
            idx += 1
        if b not in human:
            human[b] = idx
            idx += 1
        graph[human[a]].append(human[b])
        oldest[human[b]] = False
    for i in range(n):
        if oldest[i] == True:
            bfs(graph,depth,parent,i)
    q = int(input())
    for _ in range(q):
        a,b = input().rstrip().split()
        if a not in human or b not in human or parent[human[a]] != parent[human[b]] or depth[human[a]] == depth[human[b]]:
            print('gg',end=" ")
        else:
            if depth[human[a]] > depth[human[b]]:
                print(b,end=" ")
            else:
                print(a,end=" ")

def bfs(graph,depth,parent,start):
    queue = deque([start])
    depth[start] = 0
    parent[start] = start
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if depth[nx] == -1:
                depth[nx] = depth[vx] + 1
                parent[nx] = start
                queue.append(nx)
    
if __name__ == "__main__":
    main()