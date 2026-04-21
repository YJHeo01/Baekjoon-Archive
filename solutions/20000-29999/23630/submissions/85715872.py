INF = 1000001

n = int(input())

num_list = list(map(int,input().split()))

array = [[INF] * n for _ in range(21)]

answer = [0] * 21

def solution(right,value,array,j):
    ret_value = right
    left = 0
    idx = 0
    while left <= right:
        mid = (left + right) // 2
        if array[j][mid] > value:
            idx = mid
            right = mid - 1
        elif array[j][mid] < value:
            left = mid + 1
        else:
            idx = mid
            break
    if array[j][idx] == INF:
        ret_value += 1
    array[j][idx] = value
    return ret_value

for i in num_list:
    tmp = i
    for j in range(21):
        if (tmp & 1) != 0:
            answer[j] = solution(answer[j],i,array,j)
        tmp >>= 1

print(max(answer))