from collections import deque

n = int(input())

r,c = map(int,input().split())

if r == 2 and c == 2:
    print(1)
elif n % 2 == 0:
    print(n*n//2)
else:
    answer =  n * n // 2
    if (r+c) % 2 == 0: answer += 1
    print(answer)