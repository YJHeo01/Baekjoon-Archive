import sys

input = sys.stdin.readline

x,q = map(int,input().split())

array = [x]

last_value = x

for i in range(1,4):
    last_value = (last_value // i) * i + i
    array.append(last_value)

i = 3

while True:
    if array[i] - array[i-1] == array[i-1] - array[i-2] and array[i-1] - array[i-2] == array[i-2] - array[i-3]: break
    i += 1
    last_value = (last_value//i) * i + i
    array.append(last_value)
    
for _ in range(q):
    a = int(input())
    if a <= i:
        print(array[a])
    else:
        print(array[i]+(a-i)*(array[i]-array[i-1]))