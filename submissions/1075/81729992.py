n = int(input())
f = int(input())
n -= (n % 100)
for i in range(10):
    if n % f == 0:
        print("0"+str(i))
        exit(0)
    n += 1
for i in range(90):
    if n % f == 0:
        print(10+i)
        break
    n += 1