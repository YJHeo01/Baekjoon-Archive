from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    possible_root = [True] * (n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        tree[a].append(b); tree[b].append(a)
    a,b,x = map(int,input().split())
    if a != x: bfs(tree,possible_root,a,x)
    if b != x: bfs(tree,possible_root,b,x)
    answer = 0
    for i in range(1,n+1):
        if possible_root[i]: answer += 1
    print(answer)

def bfs(graph,possible_root,start,block):
    queue = deque([start])
    possible_root[start] = False
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if nx == block or possible_root[nx] == False: continue
            possible_root[nx] = False
            queue.append(nx)

if __name__ == "__main__":
    main()