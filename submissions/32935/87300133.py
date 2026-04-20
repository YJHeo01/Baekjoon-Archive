n = int(input())

array = sorted(list(map(int,input().split())))

sum_value = sum(array)

for i in range(n):
    while True:
        tmp = -sum_value - array[i]
        if tmp <= 0:
            break
        sum_value -= array[i]
        array[i] += tmp
        sum_value += array[i]

print(sum_value)