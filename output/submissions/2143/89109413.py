t = int(input())

n = int(input())

a = list(map(int,input().split()))

A_prefix_sum = [0] * (n+1)

for i in range(n):
    A_prefix_sum[i+1] = A_prefix_sum[i] + a[i]

m = int(input())

b = list(map(int,input().split()))

B_prefix_sum = [0] * (m+1)

for i in range(m):
    B_prefix_sum[i+1] = B_prefix_sum[i] + b[i]

table = dict()

for i in range(1,n+1):
    for j in range(i):
        value = A_prefix_sum[i] - A_prefix_sum[j]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
            
answer = 0

for i in range(1,m+1):
    for j in range(i):
        target = t - (B_prefix_sum[i]-B_prefix_sum[j])
        if target in table:
            answer += table[target]

print(answer)