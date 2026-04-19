n = int(input())
tmp = 2
while True:
    if n == 1: break
    while True:
        if n % tmp != 0: break
        n = n // tmp
        print(tmp)
    tmp += 1