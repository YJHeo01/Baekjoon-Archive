n = int(input())

arr = input()

for answer in range(10):
    target = arr[-1]
    if target == 'x': target = answer
    else: target = int(target)
    sum_value = 0
    for i in range(n-1):
        if arr[n-2-i] == 'x': tmp = answer
        else: tmp = int(arr[n-2-i])
        if i % 2 == 0: tmp += tmp
        if tmp >= 10:
            tmp = tmp // 10 + tmp % 10
        sum_value += tmp
    sum_value *= 9
    sum_value %= 10
    if sum_value == target:
        print(answer)
        break