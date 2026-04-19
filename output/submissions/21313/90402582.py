n = int(input())

last_value = 1 + n % 2

for i in range(n-1):
    print(1+i%2,end=" ")
    
if last_value == 1: print(2)
else: print(3)