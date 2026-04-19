n = int(input())
array = list(map(int,input().split()))
answer = [-1] * n
value = 0
for i in range(1001):
    for j in range(n):
        if array[j] == i:
            answer[j] = value
            value += 1
print(*answer)