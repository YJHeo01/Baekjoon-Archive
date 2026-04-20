n = int(input())

array = [0]*n
array = list(map(int,input().split()))
array.sort()
sum = 0
for i in range(n):
    for j in range(i+1):
        sum += array[j]

print(sum)