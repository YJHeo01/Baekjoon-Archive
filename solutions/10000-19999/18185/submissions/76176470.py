n = int(input())

array = list(map(int,input().split()))

answer = 0

for i in range(n-2):
    if array[i] == 0:
        continue
    tmp = min(array[i:i+3])
    answer += tmp * 7
    for j in range(3):
        array[i+j] -= tmp

for i in range(n-1):
    if array[i] == 0:
        continue
    tmp = min(array[i:i+2])
    answer += tmp * 5
    for j in range(2):
        array[i+j] -= tmp

for i in range(n):
    answer += array[i] * 3

print(answer)