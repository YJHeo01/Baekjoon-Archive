password = list(input())

k = int(input()) - 1

answer = ""

tmp = 1

while password:
    c = password.pop()
    if c != '1' and c != '2' and c != '6' and c != '7':
        answer += c
        continue
    if k % 2 == 1:
        if c == '1': answer += '6'
        elif c == '2': answer += '7'
        else: answer += c
    else:
        if c == '6':answer += '1'
        elif c == '7': answer += '2'
        else: answer += c
    k //= 2

if k != 0:
    print(-1)
else:
    print(answer[::-1])