from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

table = [[]]

for _ in range(n):
    table.append(list(map(int,input().split())))

def solution(table,visited,impossible_guard):
    queue = deque([1])
    visited[1] = True
    impossible_guard[1] = True
    while queue:
        vx = queue.popleft()
        tmp = []
        for nx in table[vx]:
            if nx == vx: continue
            if nx in tmp:
                impossible_guard[nx] = True
            tmp.append(nx)
            if visited[nx] == True:
                continue
            visited[nx] = True
            queue.append(nx)
visited = [False] * (n+1)
impossible_guard = [False] * (n+1)
impossible_guard[1] = True
visited[1] = True
solution(table,visited,impossible_guard)
for e in range(1,n+1):
    if impossible_guard[e] == True:
        print("Yes")
    else:
        print("No")