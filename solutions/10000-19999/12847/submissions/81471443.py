n,m = map(int,input().split())

array = list(map(int,input().split()))

prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + array[i]

answer = 0
for i in range(m,n+1):
    answer = max(answer,prefix_sum[i]-prefix_sum[i-m])

print(answer)