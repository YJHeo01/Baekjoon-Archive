from collections import deque

prime = [True] * (10000)

prime[0] = False; prime[1] = False

for i in range(2,10000):
    if prime[i] == True:
        for j in range(2*i,10000,i):
            prime[j] = False

t= int(input())

INF = int(1e9)

def solution(prime,visited,start):
    queue = deque([start])
    visited[int(''.join(start))] = 0
    while queue:
        vx = queue.popleft()
        vx_value = int(''.join(vx))
        for i in range(4):
            for j in range(10):
                nx = vx[:i] + [str(j)] + vx[i+1:]
                if nx[0] == '0':
                    continue
                nx_value = int(''.join(nx))
                if prime[nx_value] == True and visited[nx_value] > visited[vx_value] + 1:
                    visited[nx_value] = visited[vx_value] + 1
                    queue.append(nx)

for _ in range(t):
    a,b = input().split()
    a = list(a); b = int(b)
    visited = [INF] * 10000
    solution(prime,visited,a)
    answer = visited[b]
    if answer >= INF:
        answer = "Impossible"
    print(answer)
