from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = list(input().rstrip())
    num_cnt = int(input())
    sentence = list(input().rstrip())
    array = deque([])
    tmp = -1
    error = False
    for c in sentence:
        if str.isdigit(c) == True:
            if tmp == -1:
                tmp = int(c)
            else:
                tmp = tmp * 10 + int(c)
        else:
            if tmp == -1:
                continue
            array.append(tmp)
            tmp = -1
    idx = 0
    p_length = len(p)
    while idx < p_length:
        if p[idx] == 'R':
            if idx + 1 < p_length and p[idx+1] == 'R':
                idx += 1
            else:
                array.reverse()
        else:
            if array == deque([]):
                error = True
                break
            array.popleft()
        idx += 1
    if error == True:
        print("error")
    else:
        print('[',end="")
        while array:
            num = array.popleft()
            print(num,end="")
            if array == deque([]):
                continue
            print(',',end="")
        print(']')