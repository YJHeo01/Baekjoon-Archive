import sys

input = sys.stdin.readline

t = int(input())

answer = 1

for i in range(t,1,-1):
    answer *= i
    while answer % 10 == 0:
        answer //= 10
        
answer = str(answer)

l = len(answer)

print(answer[l-5:])