import sys

num = sys.stdin.readlines()

for nums in num:
    a,b = map(int,num.split())
    print(a+b)