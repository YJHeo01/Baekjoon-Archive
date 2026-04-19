num = 0
while True:
    n = int(input())
    if n == 0: break
    num += 1
    name = [input() for _ in range(n)]
    cnt = [0] * n
    for _ in range(2*n-1):
        a,b = input().split()
        cnt[int(a)-1] += 1
    for i in range(n):
        if cnt[i] == 1:
            print(num,name[i])