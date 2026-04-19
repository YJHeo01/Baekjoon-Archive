t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + array[i]
    answer = -int(1e9)
    for left in range(n):
        for right in range(left+1,n+1):
            answer = max(answer,prefix_sum[right]-prefix_sum[left])
    print(answer)