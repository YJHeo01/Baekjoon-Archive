n,k = map(int,input().split())
array = sorted(list(map(int,input().split())))
answer = 0
for i in range(n):
    answer += array[i] * min(i,k)
print(answer)