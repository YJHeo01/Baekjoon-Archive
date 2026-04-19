input()
a=list(map(int,input().split()))
m=max(a)
print(m+(sum(a)-m)/2)