n, m = map(int,input().split())

num_list = list(map(int,input().split()))

prefix_sum = [0]*(n+1)

for i in range(0,n):
    prefix_sum[i+1] = prefix_sum[i] + num_list[i]

for i in range(m):
    a,b = map(int,input().split())
    print(prefix_sum[b]-prefix_sum[a-1])