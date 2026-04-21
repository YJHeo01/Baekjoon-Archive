a,b = map(int,input().split())

for i in range(a):
    tmp = 1
    while True:
        if tmp * 26 > i: break
        tmp *= 26
    answer = ''
    while True:
        if tmp == 0: break
        answer += chr(ord('a')+(i//tmp))
        i %= tmp
        tmp //= 26
    print(answer,end=" ")