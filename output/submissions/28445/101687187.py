color = set()
for _ in range(2):
    a,b = input().split()
    color.add(a)
    color.add(b)

color = sorted(list(color))

for a in color:
    for b in color:
        print(a,b)
