n,m = map(int,input().split())

array = list(map(int,input().split()))

prefix_sum = [0] * (n+1)

prefix_sum[n] = sum(array)

for i in range(n-1,-1,-1):
    prefix_sum[i] = prefix_sum[i+1] - array[i]

answer = 0

def search_left_idx(right_idx):
    ret_value = right_idx
    left = 0
    right = right_idx
    while left <= right:
        left_idx = (left+right) // 2
        value = prefix_sum[right_idx] - prefix_sum[left_idx]
        if value < m:
            right = left_idx - 1
        elif value > m:
            left = left_idx + 1
        else:
            ret_value = left_idx
            break
    return ret_value

for right in range(1,n+1):
    left = search_left_idx(right)
    if prefix_sum[right] - prefix_sum[left] == m:
        answer += 1

print(answer)
