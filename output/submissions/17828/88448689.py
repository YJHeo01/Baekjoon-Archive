answer = []

n,x = map(int,input().split())

value = 1

for i in range(n):
    while True:
        if value + 26 * (n-i-1) >= x or value > 26:
            break
        value += 1
    answer.append(value)
    x -= value
    if value > 26: break

if value > 26 or x <  0:
    print("!")
else:
    for i in answer:
        print(chr(ord('A')+i-1),end="")