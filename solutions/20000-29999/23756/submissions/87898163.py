n = int(input())

array = [int(input()) for _ in range(n+1)]

answer = 0

for i in range(n):
    answer += min(abs(array[i]-array[i+1]),array[i+1]+360-array[i])
print(answer)