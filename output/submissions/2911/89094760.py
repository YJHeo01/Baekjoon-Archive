import sys

input = sys.stdin.readline

answer = 0

n,m = map(int,input().split())

detect = []

for _ in range(n):
    detect.append(list(map(int,input().split())))
    
detect.sort()

last_c = 0

for p,c in detect:
    if c > last_c:
        answer += (c-last_c)
    last_c = c
    
print(answer)