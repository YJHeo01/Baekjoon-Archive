from collections import deque
import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    idx = 0
    human = {}
    younger_graph = [[] for _ in range(n)]
    root = [set([]) for _ in range(n)]
    depth = [{}for _ in range(n)]
    oldest = [True] * n
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
        oldest[human[b]] = False
    for i in range(n):
        if oldest[i] == True:
            bfs(younger_graph,depth,root,i)
    q = int(input())
    for _ in range(q):
        a,b = input().rstrip().split()
        if a not in human or b not in human:
            print('gg')
            continue
        a_idx, b_idx = human[a], human[b]
        parent_list = root[a_idx] & root[b_idx]
        if parent_list == {}:
            print('gg',end=" ")
            continue
        parent = list(parent_list)[0]
        if depth[parent][a_idx] > depth[parent][b_idx]:
            print(b,end=" ")
        else:
            print(a,end=" ")

def bfs(graph,depth,root,start):
    queue = deque([start])
    depth[start][start] = 0
    root[start].add(start)
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if nx not in depth[start]:
                depth[start][nx] = depth[start][vx] + 1
                root[nx].add(start)
                queue.append(nx)
    
if __name__ == "__main__":
    main()