n,m = map(int,input().split())

if m == 0:
    print(10**n)
    exit(0)

arr = sorted(list(map(int,input().split())))

answer = 0

for i in range(10**n):
    visited = [False] * m
    if i < 10 ** (n-1) and arr[0] == 0: visited[0] = True
    while i:
        tmp = i % 10
        for j in range(m):
            if tmp == arr[j]:
                visited[j] = True
                break
        i //= 10
    for j in range(m):
        if visited[j] == False:
            answer -= 1
            break
    answer += 1

print(answer)