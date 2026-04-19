answer = -1

x = int(input())

for i in range(x+1,10000):
    a = i // 100
    b = i % 100
    if (a + b) ** 2 == i: answer = i; break
    
print(answer)