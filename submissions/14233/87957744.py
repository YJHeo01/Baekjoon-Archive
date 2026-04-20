n = int(input())
array = sorted(list(map(int,input().split())))
answer = array[n-1] // n
for i in range(n):
    if array[i] < (array[n-1] // n) * (i+1):
        answer = min(answer,array[i]//(i+1))
print(answer)