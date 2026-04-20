n,k = map(int,input().split())
array = [0] + list(map(int,input().split()))
i = 1
sum = 0
while(i<=k):
    sum += array[i]
    i+=1
answer = sum
while(i<=n):
    sum -= array[i-k]
    sum += array[i]
    answer = max(answer,sum)
    i+=1
print(answer)