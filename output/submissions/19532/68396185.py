a,b,c,d,e,f = map(int,input().split())

b,c = b*d,c*d
e,f = a*e,a*f

y = (c-f) // (b-e)

x = (c-b*y) // (a*d)

print(x,y)
