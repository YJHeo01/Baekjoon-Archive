import sys

input = sys.stdin.readline

from collections import deque

t = int(input())

for i in range(t):
    p = list(input().rstrip())
    n = int(input())
    tmp = input()
    array = deque([])
    error = 0
    for i in range(n):
        array.append(int(tmp[1+2*i]))
    l = len(p)
    for i in range(l):
        if p[i] == 'R':
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