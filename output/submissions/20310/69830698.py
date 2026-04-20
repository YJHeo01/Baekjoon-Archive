s = list(input())
zero_cnt = 0
one_cnt = 0
for c in s:
    if c == '0':
        zero_cnt += 1
    else:
        one_cnt += 1

zero_cnt = zero_cnt // 2
one_cnt = one_cnt // 2

l = len(s)
start = l-1
for _ in range(zero_cnt):
    for i in range(start,-1,-1):
        if s[i] == '0':
            s[i] = 'x'
            start = i-1
            break

start = 0
for _ in range(one_cnt):
    for i in range(start,l):
        if s[i] == '1':
            s[i] = 'x'
            start = i + 1
            break

for c in s:
    if c != 'x':
        print(c,end="")