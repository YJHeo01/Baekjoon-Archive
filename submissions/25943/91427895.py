n = int(input())

arr = list(map(int,input().split()))

weight = [0] * 2

weight[0] = arr[0]
weight[1] = arr[1]

for i in range(2,n):
    if weight[0] <= weight[1]:
        weight[0] += arr[i]
    else:
        weight[1] += arr[i]

tmp = abs(weight[1]-weight[0])

answer = 0

for i in [100,50,20,10,5,2,1]:
    answer += tmp // i
    tmp %= i

print(answer)