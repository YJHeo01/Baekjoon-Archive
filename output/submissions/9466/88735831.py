import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    array = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    possible_start = [False] * (n+1)
    for i in range(1,n+1):
        possible_start[array[i]] = True
    for start in range(1,n+1):
        if visited[start] or possible_start[start] == False: continue
        stack = [start]
        visited[start] = True
        vx = start
        result = True
        while True:
            nx = array[vx]
            if nx == start: break
            if visited[nx] or nx < start: result = False; break
            visited[nx] = True
            vx = nx
            stack.append(nx)
        if result: continue
        while stack:
            visited[stack.pop()] = False
    answer = 0
    for i in range(1,n+1):
        if visited[i] == False: answer += 1
    print(answer)