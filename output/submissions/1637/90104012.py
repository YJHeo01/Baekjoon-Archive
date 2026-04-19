import sys

input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    a,c,b = map(int,input().split())
    if a > c:
        a,c = c,a
    array.append([a,c,b])
left, right = 1, 2147483647

answer = -1

while left <= right:
    mid = (left+right) // 2
    tmp = 0
    for a,c,b in array:
        if a > mid: continue
        tmp += (min(c,mid) - a+1) // b
    if tmp % 2 == 1:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
        
if answer == -1:
    print("NOTHING")
else:
    print(answer,end=" ")
    tmp = 0
    for a,c,b in array:
        if answer < a or answer > c: continue
        if (answer-a) % b == 0:
            tmp += 1
    print(tmp)