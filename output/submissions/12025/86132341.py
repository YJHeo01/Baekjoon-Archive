password = input()
k = int(input())
cnt = 0
for i in password:
    if i == '1' or i == '2' or i == '6' or i == '7': cnt += 1

if k >= 2 ** cnt:
    print(-1)
    exit(0)

k -= 1
idx = 0

for i in password:
    if i == '1' or i == '6':
        if (1 << idx) & k: print(1,end="")
        else: print(6,end="")
    elif i == '2' or i == '7':
        if (1 << idx) & k: print(2,end="")
        else:print(7,end="")
    else:
        print(i,end="")
        continue
    idx += 1