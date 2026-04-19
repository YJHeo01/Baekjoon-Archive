import sys

sys.setrecursionlimit(5003)
input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    distance = [-1] * (n+1)
    distance[1] = 0
    answer = solution(graph,distance,1)
    print(answer)

def solution(graph,distance,vx):
    ret_value = distance[vx]
    for nx,dd in graph[vx]:
        if distance[nx] == -1:
            distance[nx] = distance[vx] + dd
            ret_value = max(ret_value,solution(graph,distance,nx))
    return ret_value

if __name__ == "__main__":
    main()