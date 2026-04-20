n,d,k = map(int,input().split())

s = list(map(int,input().split()))

answer = 0

array = [0] * n

for _ in range(d):
    tmp = 0
    for i in range(n):
        if array[i] + s[i] > k:
            tmp = 1
    if tmp == 1:
        for i in range(n):
            array[i] = 0
    answer += tmp
    for i in range(n):
        array[i] += s[i]

print(answer)