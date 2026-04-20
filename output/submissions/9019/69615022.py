import sys

input = sys.stdin.readline

from collections import deque

INF = 10000

def move(command,value):
    if command == 'D':
        ret_val = (2*value) % 10000
    elif command == 'S':
        ret_val =  (value-1) % 10000
    elif command == 'L':
        ret_val = (value // 1000) + (value * 10) % 10000
    else:
        ret_val = (value % 10) * 1000 + (value // 10)
    return ret_val

def bfs(visited,start,end):
    command_list = [[] for _ in range(10000)]
    shift = ['D','S','L','R']
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for i in range(4):
            nx = move(shift[i],vx)
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                command_list[nx] = command_list[vx] + [shift[i]]
                if nx == end:
                    return command_list[end]
                queue.append(nx)
    


t = int(input().rstrip())



for _ in range(t):
    visited = [INF] * INF
    a,b = map(int,input().split())
    answer = bfs(visited,a,b)
    for i in answer:
        print(i,end="")
    print()