import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    answer = 0
    chaE = int(1e9)
    left = 0
    right = n - 1
    while left < right:
        tmp = arr[left] + arr[right]
        if tmp - k > 0:
            right -= 1
        elif tmp - k < 0:
            left += 1
        else:
            left += 1; right -= 1
        if abs(k-tmp) < chaE: 
            chaE = abs(k-tmp); answer = 0
        if abs(k-tmp) == chaE: answer += 1
    print(answer)