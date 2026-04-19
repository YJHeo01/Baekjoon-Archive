import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    target = str(a * b)
    value = ""
    if a < b: a,b = b,a
    a = list(str(a))
    b = list(str(b))
    while a:
        tmp = a.pop()
        if b == []:
            value = tmp + value
        else:
            tmp_b = b.pop()
            value = str(int(tmp)*int(tmp_b)) + value
    if value == target:
        print(1)
    else:
        print(0)