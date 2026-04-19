n = int(input())
kbs1,kbs2=0,0
for i in range(n):
    tmp = input()
    if tmp=="KBS1":kbs1=i
    if tmp=="KBS2":kbs2=i
for _ in range(kbs1):print(1,end="")
for _ in range(kbs1):print(4,end="")
if kbs2<kbs1:kbs2+=1
for _ in range(kbs2): print(1,end="")
for _ in range(kbs2-1): print(4,end="")