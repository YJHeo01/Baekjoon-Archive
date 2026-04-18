import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    b,x,y = map(int,input().split())
    arr = []
    while True:
        if x == 0 and y == 0: break
        tmp = (x%b) + (y%b)
        tmp %= b
        arr.append(tmp)
        x //= b; y //= b
    answer = 0
    while arr:
        answer *= b
        answer += arr.pop()
    print(answer)