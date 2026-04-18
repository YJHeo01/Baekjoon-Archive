import sys

input = sys.stdin.readline

n,k = map(int,input().split())

nums = dict()

for _ in range(n):
    tmp = int(input())
    if tmp in nums:
        nums[tmp] += 1
    else:
        nums[tmp] = 1

for num in nums:
    if nums[num] % k != 0:
        print(num)
        break