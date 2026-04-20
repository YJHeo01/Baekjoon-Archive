n,m = map(int,input().split())

answer = 'Yes'

for i in range(m):
    k = int(input())
    array = list(map(int,input().split()))
    for j in range(1,k):
        if array[j-1] < array[j]:
            answer = 'No'
            
            
print(answer)