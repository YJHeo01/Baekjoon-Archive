import sys

input = sys.stdin.readline

def main():
    n,m,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    cnt = [0] * (n+1)
    for _ in range(m):
        x,y = map(int,input().split())
        graph[y].append(x)
    for _ in range(k):
        command, a = map(int,input().split())
        if command == 1:
            for pre_build in graph[a]:
                if cnt[pre_build] == 0:
                    print("Lier!")
                    return
            cnt[a] += 1
        else:
            if cnt[a] == 0:
                print("Lier!")
                return
            cnt[a] -= 1
    print("King-God-Emperor")

if __name__ == "__main__":
    main()