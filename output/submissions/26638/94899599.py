import sys

input = sys.stdin.readline

n = int(input())

arr = [input().rstrip() for _ in range(n)]

answer = 0

for i in range(1,n):
    left_length = len(arr[i-1])
    right_length = len(arr[i])
    if right_length > left_length: continue
    if left_length == right_length:
        if arr[i] < arr[i-1]:
            arr[i] += '0'
            answer += 1
        continue
    if arr[i-1][:right_length] < arr[i][:right_length]:
        arr[i] += ('0' *(left_length-right_length))
        answer += (left_length-right_length)
    elif arr[i-1][:right_length] > arr[i][:right_length]:
        arr[i] += ('0' *(left_length-right_length+1))
        answer += (left_length-right_length+1)
    else:
        if arr[i-1][right_length:] == '9' * (left_length-right_length):
            arr[i] += ('0' *(left_length-right_length+1))
            answer += (left_length-right_length+1)
        else:
            arr[i] += str(int(arr[i-1][left_length:])+1)
            answer += (left_length-right_length)  
            
print(answer)