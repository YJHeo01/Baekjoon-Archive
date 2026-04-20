n = int(input())

target = 0

answer = 0

array = [0] + list(map(int,input().split()))

for i in range(1,n+1):
    tmp = 0
    for j in range(i,n+1,i):
        tmp += array[j]
    if tmp > answer:
        target = i
        answer = tmp
    
print(target,answer)