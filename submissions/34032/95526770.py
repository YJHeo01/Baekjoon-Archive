n = int(input())

s = input()

cnt = 0

for c in s:
    if c == 'O': cnt += 1
    
if cnt * 2 >= n:print("Yes")
else: print("No")