n = int(input())

remove = [False] * n

array = list(map(int,input().split()))

answer = 0

high = 0
low = 1

while True:
    if array[high] > array[low]:
        answer += 1
        remove[low] = True
        low -= 1
    else:
        while True:
            high += 1
            if high >= n or remove[high] == False:
                break
        low = high + 1
    if low >= n:
        break

if answer > n // 2:
    answer = n - answer

print(answer) 