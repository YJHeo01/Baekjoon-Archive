a,b = map(int,input().split())

tmp = b

answer = 0

while True:
    if tmp == 1: break
    answer += 1
    if tmp % 2 != 0:
        print(-1)
        exit(0)
    tmp //= 2


for i in range(answer):    
    if ((1 << i) & a) != 0: print('G',end="")
    print('K',end="")