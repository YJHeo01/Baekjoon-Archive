import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    destroy = [False] * (n+1)
    graph = get_graph(n,m)
    k = int(input())
    destroyed_city = list(map(int,input().split()))
    for i in destroyed_city:
        destroy[i] = True
    target = [True] * (n+1)
    for i in range(1,n+1):
        if destroy[i] == False:
            target[i] = False
            for j in graph[i]:
                target[j] = False
    cnt = 0
    city_list = []
    for i in range(1,n+1):
        if target[i] == True:
            cnt += 1
            city_list.append(i)
            destroy[i] = False
            for j in graph[i]:
                destroy[j] = False
    for i in range(1,n+1):
        if destroy[i] == True:
            print(-1)
            return
    print(cnt)
    for i in city_list:
        print(i,end=" ")

def get_graph(n,m):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

if __name__ == "__main__":
    main()
