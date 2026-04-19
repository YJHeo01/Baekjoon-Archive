n = int(input())
answer = int(1e11)
array = sorted(list(map(int,input().split())))
for i in range(1,n):
    answer = min(answer,array[i]-array[i-1])
print(answer)