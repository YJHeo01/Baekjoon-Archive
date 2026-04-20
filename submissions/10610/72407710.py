num = list(input())

num.sort(reverse=True)

zero_cnt = 0
value_sum = 0

for i in num:
    if i == '0':
        zero_cnt += 1
    value_sum += int(i)

if zero_cnt == 0 or value_sum % 3 != 0:
    print(-1)
else:
    for i in num:
        print(i,end="")