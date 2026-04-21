import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    animal = [0] * (n+1)
    cnt = [0] * (n+1)
    for i in range(2,n+1):
        t,a,p = input().split()
        animal[i] = t
        cnt[i] = int(a)
        graph[int(p)].append(i)
    answer = dfs(graph,animal,cnt,1)
    print(answer)

def dfs(graph,animal,cnt,vx):
    ret_value = 0
    for nx in graph[vx]:
        ret_value += dfs(graph,animal,cnt,nx)
    if animal[vx] == 'S': ret_value += cnt[vx]
    else: ret_value -= cnt[vx]
    return max(ret_value,0)

if __name__  == "__main__":
    main()