for _ in range(int(input())):
    s = list(input())
    num_list = []
    for i in s:
        if i == '6': num_list.append(9)
        else: num_list.append(int(i))
    num_list.sort()
    num_a, num_b = 0,0
    while num_list:
        num = num_list.pop()
        if num_b > num_a:
            num_a *= 10
            num_a += num
        else:
            num_b *= 10
            num_b += num
    print(num_a*num_b)