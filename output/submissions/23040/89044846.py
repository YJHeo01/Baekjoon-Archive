from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b); tree[b].append(a)

color = ['0'] + list(input().rstrip())

answer = 0

def bfs(tree,color,visited,start):
    red_cnt = 1
    black_cnt = 0
    visited[start] = True
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        for nx in tree[vx]:
            if color[nx] == 'B':
                black_cnt += 1
            else:
                if visited[nx] == False:
                    visited[nx] = True
                    red_cnt += 1
                    queue.append(nx)
    return red_cnt * black_cnt

answer = 0

visited = [False] * (n+1)

for i in range(1,n+1):
    if color[i] == 'R' and visited[i] == False:
        answer += bfs(tree,color,visited,i)

print(answer)