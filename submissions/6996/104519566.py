n = int(input())

for _ in range(n):
    a,b = input().split()
    if len(a) != len(b):
        print(a,'&',b,'are NOT anagrams.')
        continue
    a_d = dict()
    b_d = dict()
    for c in a:
        if c in a_d:
            a_d[c] += 1
        else:
            a_d[c] = 1
    for c in b:
        if c in a_d:
            a_d[c] -= 1
        else:
            a_d[c] = -1
    answer = 1
    for c in a_d:
        if a_d[c] != 0:
            answer = 0
    if answer == 1:
        print(a,'&',b,'are anagrams.')
    else:
        print(a,'&',b,'are NOT anagrams.')