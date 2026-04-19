n,m = map(int,input().split())

array = list(map(int,input().split()))

prefix_sum = [0] * (n+1)

prefix_sum[n] = sum(array)

for i in range(n-1,-1,-1):
    prefix_sum[i] = prefix_sum[i+1] - array[i]

answer = 0

for right in range(1,n+1):
    for left in range(right):
        tmp = prefix_sum[right] - prefix_sum[left]
        if tmp > m:
            continue
        elif tmp < m:
            break
        else:
            answer += 1

print(answer)