from collections import deque
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    array = list(input().rstrip())
    num_list = deque([])
    tmp = 0
    for i in array:
        if i.isdigit() == True:
            tmp *= 10
            tmp += int(i)
        else:
            num_list.append(tmp)
            tmp = 0
    num_list.popleft()
    if n == 0:
        num_list = deque([])
    error = False
    reverse = False
    for command in p:
        if command == 'R':
            if reverse == True:
                reverse = False
            else:
                reverse = True
        else:
            if num_list == deque([]):
                error = True
                break
            if reverse == True:
                num_list.pop()
            else:
                num_list.popleft()
    if error == True:
        print('error')
    else:
        if reverse == True:
            num_list.reverse()
        print('[',end="")
        while num_list:
            value = num_list.popleft()
            print(value,end="")
            if num_list != deque([]):
                print(",",end="")
        print(']')