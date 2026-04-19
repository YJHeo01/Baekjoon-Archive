s = list(input())
t = list(input())
if len(s) > len(t):
    s,t = t,s
answer = 1
s_length, t_length = len(s), len(t)

for i in range(t_length):
    j = i % s_length
    if s[j] != t[i]:
        answer = 0

print(answer)