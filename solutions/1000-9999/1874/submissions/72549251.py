import sys

input = sys.stdin.readline

n = int(input())

def solution(n):
    last = 0
    ret_value = []
    stack = []
    for _ in range(n):
        value = int(input())
        while True:
            if stack == [] or stack[-1] < value:
                last += 1
                stack.append(last)
                ret_value.append('+')
            elif stack[-1] > value:
                return "NO"
            else:
                stack.pop()
                ret_value.append('-')
                break
    return ret_value

answer = solution(n)

if answer == 'NO':
    print(answer)
else:
    for i in answer:
        print(i)