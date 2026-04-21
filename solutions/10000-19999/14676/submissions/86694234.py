import sys

input = sys.stdin.readline

def main():
    n,m,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    need_pre_build = [0] * (n+1)
    visited = [False] * (n+1)
    cnt = [0] * (n+1)
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        need_pre_build[y] += 1
    for _ in range(k):
        command, a = map(int,input().split())
        if command == 1:
            if need_pre_build[a] != 0 and cnt[a] == 0:
                print("Lier")
                return
            cnt[a] += 1
            if visited[a]: continue
            visited[a] = True
            for nx in graph[a]:
                need_pre_build[nx] -= 1
        else:
            if cnt[a] == 0:
                print("Lier!")
                return
            cnt[a] -= 1
            if cnt[a] == 0:
                visited[a] = False
                for nx in graph[a]:
                    need_pre_build[nx] += 1
    print("King-God-Emperor")

if __name__ == "__main__":
    main()