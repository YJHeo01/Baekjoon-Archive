name = list(input())

eng = [0] * 26
for c in name:
    eng[ord(c)-ord('A')] += 1
middle = -1
impossible = -1
for i in range(26):
    if eng[i] % 2 == 1:
        middle = i
        impossible += 1
        eng[i] -= 1

if impossible >= 1:
    print("I'm Sorry Hansoo")
else:
    for i in range(26):
        if eng[i] != 0:
            eng[i] = eng[i] // 2
            for _ in range(eng[i]):
                print(chr(ord('A')+i),end="")
    if middle != -1:
        print(chr(ord('A')+middle),end="")
    for i in range(25,-1,-1):
        if eng[i] != 0:
            for _ in range(eng[i]):
                print(chr(ord('A')+i),end="")