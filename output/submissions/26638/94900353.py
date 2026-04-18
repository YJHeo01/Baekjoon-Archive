import sys

input = sys.stdin.readline

n = int(input())

arr = [input().rstrip() for _ in range(n)]

answer = 0

left = arr[0]

for right in arr[1:]:
    left_length = len(left)
    right_length = len(right)
    if right_length > left_length: 
        left = right
        continue
    if left_length == right_length:
        if left >= right:
            right += '0'
            answer += 1
        left = right
        continue
    if left[:right_length] < right[:right_length]:
        right += ('0' *(left_length-right_length))
        answer += (left_length-right_length)
    elif left[:right_length] > right[:right_length]:
        right += ('0' *(left_length-right_length+1))
        answer += (left_length-right_length+1)
    else:
        if left[right_length:] == '9' * (left_length-right_length):
            right += ('0' *(left_length-right_length+1))
            answer += (left_length-right_length+1)
        else:
            tmp = left[right_length:]
            length = len(tmp)
            idx = length - 1
            while True:
                if tmp[idx] != '9':
                    right += tmp[:idx] + chr(ord(tmp[idx])+1) + '0' * (length - idx - 1)
                    break
                idx -= 1
            answer += (left_length-right_length)  
    left = right
print(answer)