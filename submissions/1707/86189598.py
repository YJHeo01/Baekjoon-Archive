from collections import deque
import sys

input = sys.stdin.readline

def main():
    k = int(input())
    for _ in range(k):
        soluton()

def soluton():
    v,e = map(int,input().split())
    graph = [[]for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    state = [-1] * (v+1)
    answer = 'YES'
    for i in range(1,v+1):
        if state[i] != -1: continue
        answer = bfs(graph,state,i)
        if answer == 'NO': break
    print(answer)

def bfs(graph,state,start):
    queue = deque([start])
    state[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if state[nx] == state[vx]: return 'NO'
            if state[nx] == -1:
                state[nx] = (state[vx] + 1) % 2
                queue.append(nx)
    return 'YES'

if __name__ == "__main__":
    main()