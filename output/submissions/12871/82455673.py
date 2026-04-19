s = list(input())
t = list(input())

if len(s) > len(t):
    s,t = t,s

answer = 1
s_length, t_length = len(s), len(t)

def Euclidean(a,b):
    if b == 0:
        return a
    return Euclidean(b,a%b)

length = s_length * t_length // Euclidean(t_length,s_length)

for i in range(length):
    s_idx = i % s_length
    t_idx = i % t_length
    if s[s_idx] != t[t_idx]:
        answer = 0

print(answer)