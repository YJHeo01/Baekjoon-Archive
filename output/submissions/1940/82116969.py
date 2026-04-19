n = int(input())
m = int(input())
answer = 0
array = list(map(int,input().split()))
for right in range(1,n):
    for left in range(right):
        if array[left] + array[right] == m:
            answer += 1
print(answer)