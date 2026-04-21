p, m = map(int,input().split())

room = []

for _ in range(p):
    l,n = input().split()
    l = int(l)
    matching = 0
    if room != []:
        for r in room:
            if abs(r[0][0] - l) <= 10 and len(r) < 5:
                r.append((l,n))
                matching = 1
                break
    if matching == 0:
        room.append([(l,n)])

for r in room:
    if len(r) == 5:
        print("Started")
    else:
        print("Waiting!")
    for player in r:
        print(player[0],player[1])
