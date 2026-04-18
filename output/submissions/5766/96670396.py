while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0: break
    arr = [0] * 10001
    for _ in range(n):
        tmp = list(map(int,input().split()))
        for i in range(m):
            arr[tmp[i]] += 1
    rank = []
    for i in range(10001):
        rank.append((arr[i],-i))
    rank.sort(reverse=True)
    for i in range(1,10001):
        if rank[i][0] == rank[1][0]:
            print(-rank[i][1],end=" ")
        else:
            break
    print()