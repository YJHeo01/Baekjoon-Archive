r1,c1 = -1,-1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for x in range(0,9):
    for y in range(x%2,9,2):
        print("? " + str(x) + " "+ str(y))
        n = int(input())
        if n == 1:
            r1,c1 = x,y
            break
    if r1 != -1:
        break


if r1 == -1:
    for i in range(1,10,2):
        print("? " + str(i) + " 9")
        n = int(input())
        if n == 1:
            r1,c1 = i,9
            break
        print("? 9 "+str(i))
        n = int(input())
        if n == 1:
            r1,c1 = 9,i
            break

r2, c2 = -1,-1

for i in range(4):
    r2 = r1 + dx[i]
    c2 = c1 + dy[i]
    if r2 < 0 or c2 < 0 or r2 > 9 or c2 > 9:
        continue
    print("? " + str(r2) + " "+ str(c2))
    n = int(input())
    if n == 1:
        break

print("! " + str(r1) + " " + str(c1) + " " + str(r2) + " " + str(c2))