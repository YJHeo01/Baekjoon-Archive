n = int(input())

array = list(map(int,input().split()))

answer = 0

for i in range(n):
    if array[i] == 0:
        continue
    if i <= n - 3:
        tmp = min(array[i:i+3])
        answer += tmp * 7
        for j in range(3):
            array[i+j] -= tmp
    if array[i] == 0:
        continue
    if i <= n - 2:
        tmp = min(array[i:i+2])
        answer += tmp * 5
        for j in range(2):
            array[i+j] -= tmp
    answer += array[i] * 3

print(answer)