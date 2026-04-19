import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    array = [0] + list(map(int,input().split()))
    answer = 0
    visited = [False] * (n+1)
    stack = []
    for start in range(1,n+1):
        if visited[start] == False:
            stack.append(start)
            vx = start
            tmp = 0
            while True:
                nx = array[vx]
                if nx == start:
                    visited[vx] = True
                    break
                if visited[nx]:
                    tmp = 1
                    break
                visited[vx] = True
                stack.append(nx)
                vx = nx
            if tmp == 1:
                while stack:
                    visited[stack.pop()] = False
                answer += 1
            visited[start] = True
    print(answer)