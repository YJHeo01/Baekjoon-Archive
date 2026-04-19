from collections import deque

def main():
    n = int(input())
    adj_node_cnt = [0] * (n+1)
    graph = get_graph(n,adj_node_cnt)
    time = [-1] * (n+1)
    m = int(input())
    start = list(map(int,input().split()))
    solution(graph,time,start,adj_node_cnt)
    for i in range(1,n+1):
        print(time[i],end=" ")

def get_graph(n,adj_node_cnt):
    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        tmp = list(map(int,input().split()))
        tmp.pop()
        for j in tmp:
            adj_node_cnt[i] += 1
            graph[i].append(j)
    return graph

def solution(graph,time,start,adj_node_cnt):
    queue = deque(start)
    for x in start:
        time[x] = 0
    while queue:
        vx = queue.popleft()
        one_more_time = False
        for nx in graph[vx]:
            if time[nx] != -1: continue
            rumor_cnt = 0
            for nnx in graph[nx]:
                if time[nnx] == -1:continue
                if time[vx] >= time[nnx] : rumor_cnt += 1
            if rumor_cnt * 2 >= adj_node_cnt[nx]:
                time[nx] = time[vx] + 1
                queue.append(nx)
            else:
                one_more_time = True
        if one_more_time == True:
            queue.append(vx)

if __name__ == "__main__":
    main()