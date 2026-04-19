n = int(input())

array = list(map(int,input().split()))

start, mid, end = 0, 0, n-1

value = n
answer = [0] * n

for i in array:
    if i == 1:
        answer[start] = value
        while True:
            if start == n or answer[start] == 0: break
            start += 1
    elif i == 2:
        if start >= mid: mid = start + 1
        answer[mid] = value
        mid += 1
    else:
        answer[end] = value
        end -= 1
    value -= 1

print(*answer)