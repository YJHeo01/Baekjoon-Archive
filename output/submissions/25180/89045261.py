n = int(input())

answer = n // 18 * 2

tmp = n % 18

if tmp == 0:
    tmp = tmp
elif tmp <= 9:
    answer += 1
elif tmp % 2 == 0:
    answer += 2
else:
    answer += 3

print(answer)