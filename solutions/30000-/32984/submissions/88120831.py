n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

array = []

for i in range(n):
    array.append([a[i],b[i]])

array.sort(key=lambda x:(-x[1],-x[0]))

answer = 0

for i in range(n):
    array[i][0] -= answer * array[i][1] 
    if array[i][1] >= array[i][0]: continue
    answer += array[i][0] // (2 * array[i][1])

print(answer)