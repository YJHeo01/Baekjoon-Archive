import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    answer = 1
    for i in range(n):
        if answer == array[i]:
            answer += 1
        answer += 1
    answer -= 1
    print(answer)