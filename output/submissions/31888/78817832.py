from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

table = [[]]

for _ in range(n):
    table.append(list(map(int,input().split())))

def solution(table,visited,start):
    queue = deque([start])
    visited[start] = True
    while queue:
        vx = queue.popleft()
        guard = True
        for nx in table[vx]:
            if visited[nx] == True:
                continue
            if e == nx:
                if guard == True:
                    guard = False
                    continue
            visited[nx] = True
            queue.append(nx)
    
for e in range(1,n+1):
    visited = [False] * (n+1)
    solution(table,visited,1)
    if visited[e] == True:
        print("Yes")
    else:
        print("No")