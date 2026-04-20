while(1):
    m = ['a','e','i','o','u']
    r2_m,r2_j = 0,0
    pw = list(input())
    if pw[:3] == ['e','n','d']:
        break
    l = len(pw)
    r1,r2,r3 = 1,0,0
    for i in range(l):
        if pw[i] in m:
            r1 = 0
            r2_m += 1
            r2_j = 0
        else :
            r2_m = 0
            r2_j += 1
        if r2_m >= 3 or r2_j >= 3:
            r2 = 1
            break
    if l > 1:
        for i in range(l-1):
            if pw[i] == pw[i+1]:
                if pw[i] != 'o' and pw[i] != 'e':
                    r3 = 1
                    break
    if r1 + r2 + r3 >= 1:
        print("<", end = '') 
        for i in range(l):
            print(pw[i],end='')
        print("> is not acceptable")
        r1,r2,r3 = 1,0,0
    else : 
        print("<", end = '') 
        for i in range(l):
            print(pw[i],end='')
        print("> is acceptable")