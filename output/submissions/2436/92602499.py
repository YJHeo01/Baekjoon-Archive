a,b = map(int,input().split())

def euclidean(a,b):
    if b == 0: return a
    return euclidean(b,a%b)

x,y = 0, int(1e9)

for i in range(1,10001):
    if (b // a) % i == 0:
        j = b // a // i
        if j*a + i*a > y*a + x*a: continue
        if i * j * a != b or euclidean(i,j) != 1: continue
        x,y = i,j

if x > y: x,y = y,x

print(a*x,a*y)