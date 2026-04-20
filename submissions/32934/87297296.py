import sys

input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        degree[a] += 1; degree[b] += 1
        graph[a].append(b); graph[b].append(a)
    for vx in range(1,n+1):
        if degree[vx] == 3: continue
        if degree[vx] != 1:
            print(-1)
            return
        for nx in graph[vx]:
            if degree[nx] != 3:
                print(-1)
                return
    degree_three_cnt = 0
    for i in range(1,n+1):
        if degree[i] == 3: degree_three_cnt += 1
    if degree_three_cnt == n:
        print(n)
        for i in range(1,n+1):
            print(i,end=" ")
    elif degree_three_cnt != 1:
        print(-1)
    else:
        print(1)
        for i in range(1,n+1):
            if degree[i] == 3:
                print(i)
                break

if __name__ == "__main__":
    main()