for _ in range(int(input())):
    min_value = 101
    sum_value = 0
    for i in list(map(int,input().split())):
        if i % 2 == 0:
            min_value = min(min_value,i)
            sum_value += i
    print(sum_value,min_value)