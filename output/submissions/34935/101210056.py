n = int(input())

arr = list(map(int,input().split()))

answer = 1

for i in range(1,n):
    if arr[i-1] == arr[i]:
        answer = 0
        
print(answer)