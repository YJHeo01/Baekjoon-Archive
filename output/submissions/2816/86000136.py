a,b=0,0
for i in range(int(input())):
    t = input()
    if t=="KBS1":a=i
    if t=="KBS2":b=i
for _ in range(a):print(1,end="")
for _ in range(a):print(4,end="")
if b<a:b+=1
for _ in range(b): print(1,end="")
for _ in range(b-1): print(4,end="")