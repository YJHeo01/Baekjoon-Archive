import sys

input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    edge_cnt = [0] * (n+1)
    for _ in range(n):
        tmp = list(map(int,input().split()))
        idx = tmp[0]
        tmp = tmp[1:]
        tmp.pop()
        while tmp:
            edge_cnt[idx] += 1
            distance = tmp.pop()
            next_idx = tmp.pop()
            graph[idx].append((next_idx,distance))
    answer = 0
    for i in range(1,n+1):
        if edge_cnt[i] > 1:continue
        distance = [-1] * (n+1)
        distance[i] = 0
        answer = max(answer,dfs(graph,distance,i))
    print(answer)

def dfs(graph,distance,vx):
    ret_value = distance[vx]
    for nx, dist in graph[vx]:
        if distance[nx] != -1:continue
        distance[nx] = distance[vx] + dist
        ret_value = max(ret_value,dfs(graph,distance,nx))
    return ret_value

if __name__ == "__main__":
    main()