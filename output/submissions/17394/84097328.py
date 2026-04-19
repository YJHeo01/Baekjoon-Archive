from collections import deque
import sys

input = sys.stdin.readline

def main():
    t = int(input())
    prime = get_prime_list()
    for _ in range(t):
        global a,b
        n,a,b = map(int,input().split())
        visited = [INF] * INF
        visited[n] = 0
        print(bfs(prime,visited,n))

def get_prime_list():
    prime = [True] * INF
    prime[0], prime[1] = False, False
    for i in range(2,100001):
        if prime[i] == False: continue
        for j in range(i+i,100001,i):
            prime[j] = False
    return prime

def bfs(prime,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        if prime[vx] == True and vx >= a and vx <= b: return visited[vx]
        for dx in [2,3]:
            nx = vx // dx
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
        for dx in [1,-1]:
            nx = vx + dx
            if nx < 0 or nx >= INF: continue
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
    return -1

if __name__ == "__main__":
    INF = 1000001
    main()