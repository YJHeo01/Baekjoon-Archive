import sys

input = sys.stdin.readline

n = int(input())

answer = 0

a,b = map(int,input().split())

for _ in range(n-1):
    x,y = map(int,input().split())
    answer += a * y
    answer += b * x
    a += x
    b += y

print(answer)