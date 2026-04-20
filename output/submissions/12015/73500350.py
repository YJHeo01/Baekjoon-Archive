INF = 1000001

n = int(input())

num_list = list(map(int,input().split()))

array = [INF] * n

answer = 0

def solution(right,value,array):
    ret_value = right
    left = 0
    idx = 0
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > value:
            idx = mid
            right = mid - 1
        elif array[mid] < value:
            left = mid + 1
        else:
            idx = mid
            break
    if array[idx] == INF:
        ret_value += 1
    array[idx] = value
    return ret_value

for i in num_list:
    answer = solution(answer,i,array)

print(answer)