n = int(input())
e = int(input())

person = [set() for _ in range(n+1)]

idx = 0

for _ in range(e):
    tmp = list(map(int,input().split()))
    k = tmp[0]
    arr = sorted(tmp[1:])
    if arr[0] == 1:
        for i in arr:
            person[i].add(idx)
        idx += 1
    else:
        for i in arr:
            for j in arr:
                person[i] |= person[j]

for i in range(1,n+1):
    if len(person[i]) == idx:
        print(i)