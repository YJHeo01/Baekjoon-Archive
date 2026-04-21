n = int(input())

arr = list(map(int,input().split()))

answer = 0

for max_value in range(3,11):
    min_value = max_value - 2
    combo = 0
    for i in range(n):
        if arr[i] < min_value or arr[i] > max_value: combo = 0
        else: combo += 1
        answer = max(answer,combo)

print(answer)