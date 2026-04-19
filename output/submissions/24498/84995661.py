n = int(input())

array = list(map(int,input().split()))

answer = 0

for i in range(1,n-1):
    answer = max(answer,array[i]+min(array[i-1],array[i+1]))

print(answer)