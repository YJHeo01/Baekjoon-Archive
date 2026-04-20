n = int(input())
array = list(map(int,input().split()))
answer = max(array[0],array[n-1])
for i in range(1,n-1):
    answer = max(answer,array[i]+min(array[i-1],array[i+1]))
print(answer)