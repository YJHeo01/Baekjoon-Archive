n = int(input())

arr = [1]

for _ in range(n-1):
    tmp = []
    last_value = -1
    cnt = 0
    for num in arr:
        if last_value != num:
            if last_value != -1:
                tmp.append(last_value)
                tmp.append(cnt)
            last_value = num
            cnt = 1
        else:
            cnt += 1
    tmp.append(last_value)
    tmp.append(cnt)
    arr = tmp

print(max(arr))