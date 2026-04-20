n = int(input())

num = [1]*(n+1)

for i in range(2,n+1):
    num[i] = num[i-1] + num[i-2]


print(num[n])
