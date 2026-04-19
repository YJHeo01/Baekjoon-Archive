n = int(input())

array = [int(input()) for _ in range(n+1)]

answer = 0

for i in range(n):
    tmp = abs(array[i]-array[i+1])
    answer += min(tmp,360-tmp)
print(answer)