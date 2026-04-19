import sys

input = sys.stdin.readline

n,m = map(int,input().split())

answer = m

array = []

for i in range(n):
    a,b = map(int,input().split())
    if a < b: continue
    array.append((b,a))
    
array.sort()

start,end = 0,0

for a,b in array:
    if a > end:
        answer += (end-start) * 2
        start = a
        end = b
    else:
        end = max(end,b)

answer += (end-start) * 2

print(answer)