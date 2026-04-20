from collections import deque
import sys

input = sys.stdin.readline

def main():
    t = int(input())
    answer = []
    for _ in range(t):
        k,m,p = map(int,input().split())
        graph, reverse_graph, indegree = init_set(m,p)
        start,strahler = get_start(indegree,m)
        topology_sort(graph,reverse_graph,indegree,strahler,start)
        answer.append((k,strahler[m]))
    answer.sort()
    for idx, num in answer:
        print(idx,num)

def init_set(m,p):
    indegree = [0] * (m+1)
    graph = [[] for _ in range(m+1)]
    reverse_graph = [[] for _ in range(m+1)]
    for _ in range(p):
        a,b = map(int,input().split())
        graph[a].append(b)
        reverse_graph[b].append(a)
        indegree[b] += 1
    return graph, reverse_graph, indegree

def get_start(indegree,m):
    start = []; strahler = [0] * (m+1)
    for i in range(1,m+1):
        if indegree[i] != 0: continue
        start.append(i)
        strahler[i] = 1
    return start, strahler

def topology_sort(graph,reverse_graph,indegree,strahler,start):
    queue = deque(start)
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            indegree[nx] -= 1
            if indegree[nx] == 0: queue.append(nx)
        if reverse_graph[vx] == []: continue
        last_max_strahler, cnt = 0, 0
        for nx in reverse_graph[vx]:
            if last_max_strahler > strahler[nx]: continue
            if strahler[nx] > last_max_strahler:
                last_max_strahler = strahler[nx]
                cnt = 1
            else: cnt += 1
        strahler[vx] = last_max_strahler
        if cnt >= 2: strahler[vx] += 1
        
if __name__ == "__main__":
    main()