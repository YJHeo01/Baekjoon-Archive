s = list(input())
t = list(input())
for _ in range(len(t)-len(s)):
    if t[-1] == 'B':
        t.pop()
        t.reverse()
    else:
        t.pop()
answer = 1
for i in range(len(t)):
    if s[i] != t[i]:
        answer = 0
        break
print(answer)