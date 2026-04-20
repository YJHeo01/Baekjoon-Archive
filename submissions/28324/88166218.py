n = int(input())

array = list(map(int,input().split())) + [int(1e10)]

answer = 0

for i in range(n-1,-1,-1):
    array[i] = min(array[i+1]+1,n-i,array[i])
    answer += array[i]
    
print(answer)