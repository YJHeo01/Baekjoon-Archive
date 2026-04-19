import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input())
    left, right = 1, 10 ** 9
    answer = 1
    while left <= right:
        mid = (left+right) // 2
        tmp = mid * (mid + 1) // 2
        if tmp <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)