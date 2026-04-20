n = int(input())

s = list(input())

last_color = 'R'
blue,red = 0,0
if s[0] == 'R':
    red += 1
else :
    blue += 1
    last_color = 'B'

for i in range(1,n):
    if s[i] == 'B' and last_color == 'R':
        blue += 1
        last_color = 'B'
    elif s[i] == 'R' and last_color == 'S':
        red += 1
        last_color = 'R'

print(min(b,r)+1)