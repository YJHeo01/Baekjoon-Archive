s = input().split()
length = len(s)
start = -1
for i in range(length):
    if s[i][0] == '(':
        start = i
        break
    print(s[i],end=" ")
print()
if start == -1:
    print('-')
else:
    for i in range(start,length):
        if i == start and i == length-1:
            print(s[i][1:len(s[i])-1])
        elif i == start:
            print(s[i][1:],end=" ")
        elif i == length-1:
            print(s[i][:len(s[i])-1])
        else:
            print(s[i], end=" ")