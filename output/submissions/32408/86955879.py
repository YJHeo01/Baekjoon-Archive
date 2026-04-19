from collections import deque
import sys

sys.setrecursionlimit(10**6+10)
input = sys.stdin.readline

def main():
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b); graph[b].append(a)
    line_1 = [False] * (n+1)
    visited = [False] * (n+1)
    visited[n] = True
    get_line_1(graph,visited,n,line_1)
    not_line_1_cnt = 0
    for i in range(1,n+1):
        if line_1[i] == False:
            not_line_1_cnt += 1
    answer = 0
    for i in range(1,n+1):
        if line_1[i] == False:
            tmp = bfs(graph,line_1,i)
            answer += ((not_line_1_cnt-tmp) * tmp)
    answer = answer // 2
    print(answer)

def get_line_1(graph,visited,vx,line_1):
    if vx == 1:
        line_1[vx] = True
        return True
    for nx in graph[vx]:
        if visited[nx]: continue
        visited[nx] = True
        line_1[vx] |= get_line_1(graph,visited,nx,line_1)
    return line_1[vx]

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    ret_value = 1
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx]: continue
            visited[nx] = True
            queue.append(nx)
            ret_value += 1
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()