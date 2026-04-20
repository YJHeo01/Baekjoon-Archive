from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    student = [int(input()) for _ in range(n)]
    INF = 1000001
    prime = [True] * INF
    prime_list = []
    for i in range(2,INF):
        if prime[i]:
            prime_list.append(i)
            for j in range(i+i,INF,i):
                prime[j] = False
    cnt = [0] * INF
    for value in student: cnt[value] += 1
    graph = [[] for _ in range(INF)]
    for i in range(2,INF):
        if prime[i]: graph[i].append(1)
        for j in prime_list:
            if j >= i: break
            if i % j != 0: continue
            graph[i].append(i//j)
    for i in student:
        print(bfs(graph,[False]*INF,cnt,i))
    
def bfs(graph,visited,cnt,start):
    queue = deque([start])
    visited[start] = True
    ret_value = cnt[start] - 1
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx]: continue
            visited[nx] = True
            ret_value += cnt[nx]
            queue.append(nx)
    return ret_value

if __name__ == "__main__":
    main()