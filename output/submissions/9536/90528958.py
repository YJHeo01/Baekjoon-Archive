t = int(input())

for _ in range(t):
    s = list(input().split())
    block = set()
    while True:
        tmp = list(input().split())
        if len(tmp) == 5: break
        block.add(tmp[2])
    for c in s:
        if c in block: continue
        print(c,end=" ")
    print()