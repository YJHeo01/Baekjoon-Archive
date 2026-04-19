n,m = map(int,input().split())

answer = 1

if n >= 3:
    if m <= 4:
        answer = m
    elif m <= 6:
        answer = 4
    else:
        answer = m - 2
elif n == 2:
    answer = (m-1) // 2 + 1
    if answer > 4:
        answer = 4
else:
    answer = 1

print(answer)