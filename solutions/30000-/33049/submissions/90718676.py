impossible = True

p3,p4,p0 = map(int,input().split())

for t3 in range(100001):
    if p3 > t3 * 3: continue
    tmp = p3 + p0 - t3 * 3
    if tmp < 0: continue
    if (p4+tmp) % 4 == 0:
        print(t3,(p4+tmp)//4)
        impossible = False
        break
    
if impossible:
    print(-1)