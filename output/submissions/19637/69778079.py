import sys

input = sys.stdin.readline

n, m = map(int,input().split())
l = -1
name = []
name_ = []
for _ in range(n):
    power, num = input().split()
    if int(num) not in name_:
        name.append(power)
        name_.append(int(num))
        l += 1

for _ in range(m):
    tmp = int(input())
    left = 0
    right = l
    answer = l
    mid = -1
    while left <= right:
        tmp = (left+right) // 2
        if mid != tmp:
            mid = tmp
        else:
            break
        if name_[mid] < tmp:
            left = mid + 1
        else:
            right = mid - 1
            answer = min(answer,mid)
    print(name[answer])