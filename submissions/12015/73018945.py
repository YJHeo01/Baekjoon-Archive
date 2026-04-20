n = int(input())

length_min_list = [0] * (n+1)

answer = 0

num_list = list(map(int,input().split()))

def solution(value,answer,length_min_list):
    left, right = 0, answer
    target = answer
    while left<=right:
        mid = (left+right) // 2
        if length_min_list[mid] > value:
            left = mid + 1
            target = mid
        elif length_min_list[mid] < value:
            right = mid - 1
        else:
            target = mid
            break
    if length_min_list[target-1] != value:
        length_min_list[target] = value
    if target == answer:
        return answer + 1
    else:
        return answer
    

for i in range(n):
    answer = solution(num_list[i],answer,length_min_list)

print(answer)
