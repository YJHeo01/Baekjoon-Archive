n, m = map(int,input().split())

num_list = list(map(int,input().split()))

prefix_sum = [0]*(n+1)

answer = 0

for i in range(0,n):
    prefix_sum[i+1] = prefix_sum[i] + num_list[i]
    if prefix_sum[i+1] % m == 0:
        answer += 1

for i in range(1,n+1):
    for j in range(0,i-1):
        prefix_sum[i] -= num_list[j]
        if prefix_sum[i] % m == 0:
            answer += 1
print(answer)
