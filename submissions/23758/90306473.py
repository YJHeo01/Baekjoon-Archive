import sys

input = sys.stdin.readline

n = int(input())

array = sorted(list(map(int,input().split())))

q = []

answer = 0

for i in range(n//2+n%2):
    while True:
        if array[i] == 0: break
        answer += 1
        array[i] //= 2

if n > 2: answer -= 1

print(answer)