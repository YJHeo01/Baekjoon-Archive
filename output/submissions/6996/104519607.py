n = int(input())

for _ in range(n):
    a,b = input().split()
    answer = 1
    if len(a) != len(b):
        answer = 0
    d = dict()
    for c in a:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in b:
        if c in d:
            d[c] -= 1
        else:
            d[c] = -1
    for c in d:
        if d[c] != 0:
            answer = 0
    if answer == 1:
        print(a,'&',b,'are anagrams.')
    else:
        print(a,'&',b,'are NOT anagrams.')