s = list(input())

n = int(input())

array = list(map(int,input().split()))

last_alphabet = '?'

answer = ''

for c in s:
    if last_alphabet == c: continue
    if answer == '':
        last_alphabet = c
        if c == ' ': n -= 1
        else: answer += c.upper()
        continue
    if c == ' ':
        n -= 1
        last_alphabet = c
        continue
    tmp = c.upper()
    if last_alphabet == ' ': answer += tmp
    last_alphabet = c
    array[ord(tmp)-ord('A')] -= 1


if n < 0 or min(array) < 0:
    print(-1)
else:
    print(answer)