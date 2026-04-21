import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    num_list = set(arr)
    answer = 0
    for i in range(n):
        for j in range(i):
            b = arr[j]
            a = arr[i]
            c = 2 * b - a
            if c in num_list: answer += 1
    print(answer)