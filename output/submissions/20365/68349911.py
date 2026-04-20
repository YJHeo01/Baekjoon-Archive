n = int(input())

s = list(input())

b = 0
r = 0

for i in range(n):
    if s[i] == 'B':
        b+=1
    else:
        r+=1

print(min(b,r)+1)