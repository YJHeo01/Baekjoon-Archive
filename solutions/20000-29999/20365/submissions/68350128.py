n = int(input())

s = list(input())

color = ['R','B']

color_count = [0,0]

last_color = 'R'

if s[0] == color[0]:
    color_count[0] += 1
else :
    color_count[1] += 1
    last_color = 'B'

for i in range(1,n):
    if s[i] == 'B' and last_color == 'R':
        color_count[1] += 1
        last_color = 'B'
    elif s[i] == 'R' and last_color == 'S':
        color_count[0] += 1
        last_color = 'R'

print(min(b,r)+1)