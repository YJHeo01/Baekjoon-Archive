import math

n = int(input())

array_A = list(map(int,input().split()))

array_A.sort()

def get_plus_value_first_idx(array_A):
    ret_value = n
    left, right = 0, n-1
    while left <= right:
        mid = (left+right) // 2
        if array_A[mid] > 0:
            ret_value = mid
            right = mid - 1
        else:
            left = mid + 1
    return ret_value

def get_minus_value_last_idx(array_A):
    ret_value = -1
    left, right = 0,n-1
    while left <= right:
        mid = (left+right) // 2
        if array_A[mid] < 0:
            ret_value = mid
            left = mid + 1
        else:
            right = mid - 1
    return ret_value

minus_value_last_idx = get_minus_value_last_idx(array_A)
plus_value_first_idx = get_plus_value_first_idx(array_A)
zero_cnt = plus_value_first_idx - minus_value_last_idx - 1
answer = 0

if zero_cnt >= 3:
    answer += math.comb(zero_cnt,3)

def get_bigger_value_idx(array_A,left,right):
    ret_value = right
    original_value = array_A[left]
    while left<=right:
        mid = (left+right) // 2
        if array_A[mid] > original_value:
            ret_value = mid
            right = mid - 1
        else:
            left = mid + 1
    return ret_value

def get_smaller_value_idx(array_A,left,right):
    ret_value = left
    original_value = array_A[right]
    while left <= right:
        mid = (left+right) // 2
        if array_A[mid] < original_value:
            ret_value = mid
            left = mid + 1
        else:
            right = mid - 1
    return ret_value

def find_sum_zero_set_cnt(array_A,init_left,init_right):
    target_value = -(array_A[init_left] + array_A[init_right])
    left = init_left; right = init_right
    ret_value = 0
    left += 1; right -= 1
    mid = -1
    while left <= right:
        mid = (left+right) // 2
        if target_value > array_A[mid]:
            left = mid + 1
        elif target_value < array_A[mid]:
            right = mid - 1
        else:
            break
    if mid != -1 and array_A[mid] == target_value:
        ret_value = get_bigger_value_idx(array_A,mid,init_right) - get_smaller_value_idx(array_A,init_left,mid) - 1
    return ret_value

for left in range(minus_value_last_idx+1):
    for right in range(plus_value_first_idx,n):
        if array_A[left] + array_A[right] == 0:
            answer += zero_cnt
        else:
            answer += find_sum_zero_set_cnt(array_A,left,right)

print(answer)