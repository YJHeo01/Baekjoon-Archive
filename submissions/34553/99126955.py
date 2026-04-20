s = input()

l = len(s)

answer = 1

tmp = 1

for i in range(1,l):
    if s[i] > s[i-1]:
        tmp += 1
    else:
        tmp = 1
    answer += tmp

print(answer)