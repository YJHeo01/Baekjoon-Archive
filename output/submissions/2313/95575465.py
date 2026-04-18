import sys

input = sys.stdin.readline

n = int(input())

sum_value = 0

answer = []

for _ in range(n):
    l = int(input())
    arr = list(map(int,input().split()))
    max_value = -int(1e9)
    tmp = max_value
    left, right = 0,0
    t_l, t_r = 0,0
    while True:
        if right == l: break
        if tmp <= 0:
            tmp = 0
            left = right
        tmp += arr[right]
        if tmp > max_value:
            max_value = tmp
            t_l, t_r = left + 1, right + 1
        if tmp == max_value and (right-left) < (t_r-t_l):
            t_l, t_r = left + 1, right + 1
        right += 1
    sum_value += max_value
    answer.append((t_l,t_r))
    
print(sum_value)

for row in answer:
    print(*row)

