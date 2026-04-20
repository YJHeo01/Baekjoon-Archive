n = int(input())
a,b = map(int,input().split())
c = int(input())
t = []
for i in range(n):
    tmp = int(input())
    t.append(tmp)
t.sort(reverse=True)
cal = c
price = a
for i in range(n):
    tmp = cal + t[i]
    if cal / price < tmp / (price + b):
        cal = tmp
        price += b
    else:
        break

print(cal//price)