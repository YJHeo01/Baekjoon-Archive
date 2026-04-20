n = int(input())

arr = sorted([int(input()) for _ in range(n)])

answer = 0

for i in range(1,n-1):
    answer = max(answer,abs(arr[i]*2-arr[0]-arr[n-1]))
    
print(answer)