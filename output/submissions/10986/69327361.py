import sys

input = sys.stdin.readline

n, m = map(int,input().split())

num_list = list(map(int,input().split()))

prefix_sum = [0]*(n+1)

answer = 0

for i in range(0,n):
    prefix_sum[i+1] = prefix_sum[i] + num_list[i]
    for j in range(0,i+1):
        if (prefix_sum[i+1] - prefix_sum[j]) % m == 0:
            answer += 1

print(answer)