h, m, s= map(int, input().split())
ps = int(input())

sm = (s + ps)//60
s = (s + ps)%60
mh = (m+sm)//60
m = (m+sm)%60
h = h+mh

h %= 24

print(f'{h} {m} {s}') 