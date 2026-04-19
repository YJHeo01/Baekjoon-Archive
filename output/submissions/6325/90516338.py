num = 1

while True:
    n = int(input())
    if n == 0: break
    print("Program " + "#"+str(num))
    num += 1
    none = True
    answer = [False] * 26
    answer[0] = True
    for _ in range(n):
        x,y,z = input().split()
        a = ord(x) - ord('a')
        b = ord(z) - ord('a')
        answer[a] = answer[b]
    for i in range(26):
        if answer[i]:
            none = False
            print(chr(ord('a')+i),end=" ")
    if none:
        print("none")
    else:
        print()
    print()