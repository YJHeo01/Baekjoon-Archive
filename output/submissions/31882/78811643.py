n = int(input())

s = list(input())

answer = 0
two_length = 0
facto = 0
tmp = 0
for i in range(n):
    if s[i] == '2':
        two_length += 1
        facto += two_length
        tmp += facto
        answer += facto
    else:
        facto = 0
        tmp = 0
        two_length = 0
print(answer)