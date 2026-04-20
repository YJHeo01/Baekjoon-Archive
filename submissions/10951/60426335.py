import sys

num = sys.stdin.readlines()

for nums in num:
    a,b = map(int,nums.split())
    print(a+b)