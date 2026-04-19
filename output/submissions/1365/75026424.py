n = int(input())

array = list(map(int,input().split()))

dp = [-1] * n

def LIS(dp,value,right):
    idx = right
    ret_value = right
    left = 0
    while left <= right:
        mid = (left+right) // 2
        if dp[mid] >= value:
            idx = mid
            right = mid - 1
        else:
            left = mid + 1
    if dp[idx] == -1:
        ret_value += 1
    dp[idx] = value
    return ret_value
    
answer = 0

for i in range(n):
    value = array[i]
    answer = LIS(dp,value,answer)

answer = min(answer,n-answer)

print(answer)