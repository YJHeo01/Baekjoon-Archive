import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

answer = 0

def main():
    v = int(input())
    graph = [[] for _ in range(v+1)]
    for _ in range(v):
        tmp = list(map(int,input().split()))
        tmp.pop()
        vx = tmp[0]
        while True:
            length = tmp.pop()
            if tmp == []: break
            nx = tmp.pop()
            graph[vx].append((nx,length))
    distance = [-1] * (v+1)
    distance[1] = 0
    solution(graph,distance,1)
    print(answer)
    
def solution(graph,distance,vx):
    dist_list = [0,0]
    for nx, length in graph[vx]:
        if distance[nx] != -1: continue
        distance[nx] = distance[vx] + length
        dist_list.append(solution(graph,distance,nx))
    dist_list.sort(reverse=True)
    global answer
    answer = max(answer,sum(dist_list[:2]),distance[vx]+dist_list[0])
    return dist_list[0]

if __name__ == "__main__":
    main()