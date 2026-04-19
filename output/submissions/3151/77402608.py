n = int(input())

student = list(map(int,input().split()))

student.sort()

answer = 0

def solution(student,left,right):
    target_value = - (student[left] + student[right])
    init_left = left
    init_right = right
    left += 1; right -= 1
    ret_value = 0
    while left <= right:
        mid = (left+right) // 2
        if student[mid] < target_value:
            left = mid + 1

        elif student[mid] > target_value:
            right = mid - 1
        else:
            ret_value = 1
            break
    if ret_value == 1:
        idx = mid
        while True:
            idx += 1
            if idx == init_right or student[mid] != student[idx]:
                break
            ret_value += 1
        idx = mid
        while True:
            idx -= 1
            if idx == init_left or student[mid] != student[idx]:
                break
            ret_value += 1
    return ret_value

for left in range(n-2):
    for right in range(left+2,n):
        answer += solution(student,left,right)

print(answer)