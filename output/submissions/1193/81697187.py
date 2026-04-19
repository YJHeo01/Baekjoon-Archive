x = int(input())
for i in range(1,4473):
    if i*(i+1) // 2 >= x:
        tmp = i * (i+1) // 2
        a,b = 1+tmp-x,i-(tmp-x)
        if i % 2 == 0:
            a,b = b,a
        print(str(a)+"/"+str(b))
        break