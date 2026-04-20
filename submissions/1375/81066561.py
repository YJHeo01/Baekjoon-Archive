from collections import deque
import sys

input = sys.stdin.readline

def main():
    INF = int(1e9)
    n,m = map(int,input().split())
    idx = 0
    human = {}
    younger_graph = [[] for _ in range(n)]
    older_graph = [[] for _ in range(n)]
    younger_root = [0] * n
    older_root = [0] * n
    younger_depth = [-1] * n
    older_depth = [-1] * n
    oldest = [True] * n
    youngest = [True] * n
    for _ in range(m):
        a,b = input().rstrip().split()
        if a not in human:
            human[a] = idx
            idx += 1
        if b not in human:
            human[b] = idx
            idx += 1
        younger_graph[human[a]].append(human[b])
        older_graph[human[b]].append(human[a])
        oldest[human[b]] = False
        youngest[human[a]] = False
    for i in range(n):
        if oldest[i] == True:
            bfs(younger_graph,younger_depth,younger_root,i)
        if youngest[i] == True:
            bfs(older_graph,older_depth,older_root,i)
    q = int(input())
    for _ in range(q):
        a,b = input().rstrip().split()
        if a not in human or b not in human:
            print('gg')
            continue
        a_idx, b_idx = human[a], human[b]
        if older_root[a_idx] == older_root[b_idx] and older_depth[a_idx] != older_depth[b_idx]:
            if older_depth[a_idx] > older_depth[b_idx]:
                print(a,end=" ")
            else:
                print(b,end=" ")
        elif younger_root[a_idx] == younger_root[b_idx] and younger_depth[a_idx] != younger_depth[b_idx]:
            if younger_depth[a_idx] > younger_depth[b_idx]:
                print(b,end=" ")
            else:
                print(a,end=" ")
        else:
            print("gg")

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