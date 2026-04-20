import sys

input = sys.stdin.readline

from collections import deque

t = int(input())

for i in range(t):
    p = list(input())
    n = int(input())
    tmp = input()
    array = deque([])
    error = 0
    for i in range(n):
        array.append(int(tmp[1+2*i]))
    for c in p:
        if c == 'R':
            array.reverse()
        else:
            if array == deque([]):
                error = 1
                break
            else:
                array.popleft()
    if error == 1:
        print("error")
    else:
        print(list(array))